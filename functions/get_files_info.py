import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path,directory))

        # Evaluates to true or false due to "=="
        valid_target = os.path.commonpath([abs_path, target_dir]) == abs_path
        if not valid_target:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir): # Handels file passed instead of directories
            return f'Error: "{directory}" is not a directory'
        else: 
            return f'Success: "{directory}" is within the working directory'
    except Exception as error:
        return f'Error: {error}'