RESET = '\033[0m'
GREEN = '\033[32m'
BROWN = '\033[33m'
MAGENTA = '\033[35m'
HALF_BRIGHT = '\033[2m'
RED = '\033[31m'


class Printer:
    @staticmethod
    def model_message(content: str | None):
        if content:
            print(GREEN + content + RESET)

    @staticmethod
    def tool_call(content: str):
        print(BROWN + content + RESET)

    @staticmethod
    def tool_result(content: str):
        print(MAGENTA + content + RESET)

    @staticmethod
    def info(content: str):
        print(HALF_BRIGHT + content + RESET)

    @staticmethod
    def error(content: str):
        print(RED + content + RESET)

