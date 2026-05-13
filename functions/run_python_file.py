import os
import subprocess
import sys
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: Directory {abs_file_path} is outside the working directory {abs_working_directory}."
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {abs_file_path} is not a valid file."

    if not abs_file_path.endswith(".py"):
        return f"Error: {abs_file_path} is not a Python (.py) file."

    if args is None:
        args = ""

    try:
        result = subprocess.run(
            [sys.executable, abs_file_path, args],
            capture_output=True,
            text=True,
            cwd=abs_working_directory,
        )

        out = result.stdout.strip()
        err = result.stderr.strip()

        msg = f"Output:\n{out}\n\nErrors:\n{err}"

        if out == "" and err == "":
            msg += "\n\nNo output or errors captured."

        return msg

    except Exception as e:
        return f"Error executing file {abs_file_path}: {str(e)}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified Python file relative to the working directory with optional command-line arguments and captures its output and errors",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="String of the command-line arguments to pass to the Python script (optional)",
            ),
        },
    ),
)