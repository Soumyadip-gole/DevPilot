import os

from google.genai import types

def get_file_contents(working_directory,file_path):
    abs_working_directory=os.path.abspath(working_directory)
    abs_file_path=os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: File {abs_file_path} is outside the working directory {abs_working_directory}."
    if not os.path.isfile(abs_file_path):
        return f"Error: {abs_file_path} is not a valid file."
    
    file_contents=""
    try:
        with open(abs_file_path,'r')as f:
            file_contents=f.read()
    except Exception as e:
        return f"Error reading file {abs_file_path}: {str(e)}"
    
    return file_contents
    
schema_get_files_contents= types.FunctionDeclaration(
    name="get_files_content",
    description="gets the content of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to get contents from, relative to the working directory",
            ),
        },
    ),
)