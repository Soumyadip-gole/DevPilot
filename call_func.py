import os

from functions.get_files_contents import get_file_contents
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types

from dotenv import load_dotenv
load_dotenv()
working_directory = os.getenv("WORKING_DIRECTORY") 
def call_func(func_name, file_path,content = "", args = None):
    if func_name == "get_files_info":
        result = get_files_info(working_directory,file_path)
    elif func_name == "get_files_content":
        result = get_file_contents(working_directory,file_path)
    elif func_name == "run_python_file":
        result = run_python_file(working_directory,file_path,args)
    elif func_name == "write_file":
        result = write_file(working_directory,file_path,content)
    else:
        result = f"Error: Function {func_name} is not recognized."

    return result


# schema_call_func = types.FunctionDeclaration(
#     name="call_func",
#     description="Calls a specified function (get_files_info, get_files_content, run_python_file, write_file) with the provided file path, content, and arguments relative to the working directory",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         properties={
#             "file_path": types.Schema(
#                 type=types.Type.STRING,
#                 description="File path to run, relative to the working directory",
#             ),
#             "content": types.Schema(
#                 type=types.Type.STRING,
#                 description="Content to write to the file",
#             ),
#             "args": types.Schema(
#                 type=types.Type.STRING,
#                 description="Optional list of command-line arguments to pass to the Python script",
#             ),
#         },
#     ),
# )