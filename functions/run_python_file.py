import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path,file_path))

    valid_target = os.path.commonpath([abs_path, target_dir]) == abs_path
    if not valid_target:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target_dir):  # Handles if passed directory error
        return f'Error: "{file_path}" does not exist or is not a regular file'
    elif not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    else:
        command = ["python", file_path] # Trying to simulate Terminal [python hello.py]
        if args:
            command.extend(args)
        CompletedProcess = subprocess.run(args=command, cwd=abs_path, text=True, timeout=30, capture_output=True)

        # Build a output string now
        output = []
        if CompletedProcess.returncode:
            output.append(f"Process exited with code {CompletedProcess.returncode}")
        if not CompletedProcess.stdout and not CompletedProcess.stderr:
            output.append("No output produced")
        else:
            if CompletedProcess.stdout and CompletedProcess.stderr:
                output.append(f"STDOUT:{CompletedProcess.stdout} \n STDERR:{CompletedProcess.stderr}")
            elif CompletedProcess.stderr:
                output.append(f"STDERR:{CompletedProcess.stderr}")
            else:
                output.append(f"STDOUT:{CompletedProcess.stdout}")
        return "\n".join(output)