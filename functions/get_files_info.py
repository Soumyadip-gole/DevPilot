import os

from google.genai import types

def get_files_info(working_directory,directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    if directory == ".":
        directory=working_directory
    else:
        directory=os.path.join(working_directory,directory)
    abs_directory = os.path.abspath(directory)
    print(f"abs_working_directory: {abs_working_directory}")
    print(f"abs_directory: {abs_directory}")
    if not abs_directory.startswith(abs_working_directory):
        return f"Error: Directory {abs_directory} is outside the working directory {abs_working_directory}."
    
    result="Result for current directory: \n"
    try:
        contents=os.listdir(abs_directory)
    except FileNotFoundError:
            return [f"Error: Directory not found  {abs_directory}"]
    for content in contents:
        is_dir = os.path.isdir(os.path.join(abs_directory, content))
        file_info=os.path.getsize(os.path.join(abs_directory, content))
        result+=f" -{content}: file_size={file_info} bytes, is_dir={is_dir} \n"
    
    return result
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)