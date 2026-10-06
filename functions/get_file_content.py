import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
        try:
            abs_path = os.path.abspath(working_directory)
            target_dir = os.path.normpath(os.path.join(abs_path,file_path))

            # Evaluates to true or false due to "=="
            valid_target = os.path.commonpath([abs_path, target_dir]) == abs_path
            if not valid_target:
                return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
            elif not os.path.isfile(target_dir):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            else:
                with open(target_dir, "r") as f:
                    file_content_string = f.read(MAX_CHARS) # File .pfk/.py
                    if f.read(1): # Returns true ro false
                        file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    return file_content_string
        except Exception as Error:
            return f'Error: {Error}'
                     
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path,file_path))

        valid_target = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not valid_target:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        else:
            os.makedirs(os.path.dirname(target_dir), exist_ok=True)
                
             # Open teh file
            with open(target_dir, "w") as f:
                f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' # Feedback loops
    except Exception as error:
        return f'Error: {error}'