from ollama import chat
from tiny_harness.models.models import Model, ModelManager
from tiny_harness.tools.tools import ToolManager

print(f'')
model_manager = ModelManager()
messages = []
while True:
    question = input("")
    messages.append({'role': 'user', 'content': question})

    if question == '/model':
        print(f'You\'re currently using the model {model_manager.current_model.value}\nTo switch to a different model select the appropriate number:')
        available_models = []
        for m in Model:
            available_models.append(m)
            print(f'{len(available_models)} :  {m}')
        print('0 : Cancel')
        choice = int(input())
        if choice > 0 and choice <= len(available_models):
            model_manager.switch_model(available_models[choice - 1])
            print(f'you\'re now using the model {model_manager.current_model}')
        continue

    
    response = chat(
        model=model_manager.current_model,
        messages=messages,
        tools=[ToolManager.read]
    )
    messages.append(response.message)
    print(response.message.content)
    
    if response.message.tool_calls:
        call = response.message.tool_calls[0]
        result = ToolManager.read(**call.function.arguments)
        messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': str(result)})
        final_response = chat(model=model_manager.current_model, messages=messages, tools=[ToolManager.read], think=True)
        print(final_response.message.content)
