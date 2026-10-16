from pathlib import Path

class ToolManager:
    @staticmethod
    def read(path: str) -> str:
        """Read a file.

        Args:
            path: Relative path"""
        with open(path) as f:
            return f.read()

    @staticmethod
    def list_dir(path: str):
        """List a directory.

        Args:
            path: Has to be within the current working directory"""
        requested_path = Path(path).resolve()
        if requested_path.is_relative_to(Path.cwd()):
            result = []
            file_list = list(requested_path.iterdir())
            for file in file_list:
                if file.is_dir():
                    result.append(file.name + '/')
                else:
                    result.append(file.name)
            print(f'The agent requested a list of all files in {path}.\nThis is the result:\n{result}')
            return result
        else:
            return f'The path "{path}" is not a valid path inside the current project.'

ALL_TOOLS = [ToolManager.read, ToolManager.list_dir]
