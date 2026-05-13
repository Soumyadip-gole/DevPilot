import os
import google.genai.types as types


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    parent_dir = os.path.dirname(abs_file_path)

    #create folders if missing
    try:
        os.makedirs(parent_dir, exist_ok=True)
    except Exception as e:
        return f"Error creating directories for {abs_file_path}: {str(e)}"

    #write file
    try:
        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        return f"Error writing to file {abs_file_path}: {str(e)}"

    return f"File {abs_file_path} written successfully with length {len(content)}."

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating any necessary directories and overwriting existing files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the specified file",
            ),
        },
    ),
)