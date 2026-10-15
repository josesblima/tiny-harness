from enum import Enum

class ToolManager:
    def read(self, path: str):
        f = open(path)
        return f.read()

class Tool(Enum):
    READ = 'read'
