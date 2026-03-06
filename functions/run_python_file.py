import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        valid_file_path = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        cmd_result = subprocess.run(
            command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output = []
        if cmd_result.returncode != 0:
            output.append(f"Process exited with code {cmd_result.returncode}")
        if not cmd_result.stdout and not cmd_result.stderr:
            output.append("No output produced")
        else:
            if cmd_result.stdout:
                output.append(f"STDOUT: {cmd_result.stdout.rstrip()}")
            if cmd_result.stderr:
                output.append(f"STDERR: {cmd_result.stderr.rstrip()}")
        
        return "\n".join(output)


    except Exception as e:
        return f"Error: executing Python file: {e}"