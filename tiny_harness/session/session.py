from collections.abc import Callable
from ollama import ChatResponse, Message
from ollama import chat

from tiny_harness.models.models import Model
from tiny_harness.tools.exceptions import ToolError
from tiny_harness.tools.tools import ALL_TOOLS

class Session:
    def __init__(self, *, model: Model = Model.QWEN38, messages: list[Message] | None = None, tools: list[Callable] | None = None):
        self.model = model
        self.messages = list(messages) if messages else []
        self.tools = tools if tools is not None else ALL_TOOLS
        self.tools_dic = {fn.__name__: fn for fn in self.tools}

    def run_interactive(self):
        while True:
            user_input = input("-> ")

            if self._handle_commands(user_input = user_input):
                continue
            
            self.messages.append(Message(role = 'user', content = user_input))

            while True:
                response = chat(
                    model = self.model.value,
                    messages = self.messages,
                    tools = self.tools
                )
                self.messages.append(response.message)

                if not response.message.tool_calls:
                    print(response.message.content)
                    break
                self._handle_tool_calls(tool_calls=response.message.tool_calls)

    def run_headless(self):
        pass

    def _handle_commands(self, user_input: str):
        if user_input[0] != '/':
            return False
        if user_input == '/model':
            print(f'You\'re currently using the model {self.model.value}\nTo switch to a different model select the appropriate number:')
            available_models = []
            for m in Model:
                available_models.append(m)
                print(f'{len(available_models)} :  {m}')
            print('0 : Cancel')
            choice = int(input())
            if choice > 0 and choice <= len(available_models):
                self.model = available_models[choice - 1]
                print(f'you\'re now using the model {self.model.value}')
                return True
        return False

    def _handle_tool_calls(self, tool_calls):
        for call in tool_calls:
            fn = self.tools_dic.get(call.function.name)
            if fn is None:
                result = f'The tool {call.function.name} doesn\'t exist.'
            else:
                try:
                    result = fn(**call.function.arguments)
                except ToolError as e:
                    result = f'Error: {e}'
                except Exception as e:
                    result = f'Unexpected Error: {e}'
            self.messages.append(Message(role='tool', tool_name=call.function.name, content=str(result)))
        
