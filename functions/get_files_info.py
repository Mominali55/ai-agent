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
            is_dir = False # Done
            file_size = 0
            file_info: list[str] = []

            for item in os.listdir(target_dir):
                file_path = os.path.join(target_dir, item)
                if os.path.isdir(file_path):
                    is_dir = True
                file_size = os.path.getsize(file_path)
                file_info.append(
                    f'- {item}: file_size={file_size} bytes, is_dir={is_dir}'
                    )
            return f"Result for {directory}: \n" + "\n".join(file_info)
                
    except Exception as error:
        return f'Error: {error}'