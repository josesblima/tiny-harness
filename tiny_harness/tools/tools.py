class ToolManager:
    @staticmethod
    def read(path: str) -> str:
        """Read a file.

        Args:
            path: Relative path"""
        with open(path) as f:
            return f.read()

ALL_TOOLS = [ToolManager.read]
