from pathlib import Path

from tiny_harness.tools.exceptions import ToolError

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
            return result
        else:
            raise ToolError(f'The path "{path}" is not a valid path inside the current project.')

    @staticmethod
    def edit_file(path: str, old_str: str, new_str):
        """Edit a file. Search and replace strings. If there is more than one string that matches the old_str, pass a bigger string.

        Args:
            path: Path to the file within the current working directory
            old_str: Text to replace
            new_str: New text"""
        if not Path(path).resolve().is_relative_to(Path.cwd()):
            raise ToolError(f'The path "{path}" is not a valid path inside the current project.')
        
        p = Path(path)
        content = p.read_text()
        count = content.count(old_str)
        if count == 0:
            raise ToolError(f'There are no strings that match old_str.')
        if count > 1:
            raise ToolError(f'There are multiple results to the old string, please give more context around it.')
        
        p.write_text(content.replace(old_str, new_str))
        return f'The changes were successfully applied.'

ALL_TOOLS = [ToolManager.read, ToolManager.list_dir, ToolManager.edit_file]
