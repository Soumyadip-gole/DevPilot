import os

from dotenv import load_dotenv
from functions.get_files_contents import schema_get_files_contents
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_func import call_func
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("Gemini_api_key")
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python scripts
- Write or modify files
- Remember to handle errors gracefully and provide informative messages.

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

client = genai.Client(api_key=api_key)
history = []
available_functions = [
    schema_get_files_info,
    schema_get_files_contents,
    schema_run_python_file,
    schema_write_file,
    #schema_call_func
]
tools=[types.Tool(function_declarations=available_functions)]
config = types.GenerateContentConfig(tools=tools,system_instruction=system_prompt)


def main():
    while True:
        prompt = input("input your prompt: ")
        history.append(types.Content(role="user", parts=[types.Part(text=prompt)]))

        if prompt == "exit":
            break

        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=history,
            config=config,
        )

        if response.candidates and response.candidates[0].content:
            history.append(response.candidates[0].content)


        if response.function_calls:
            for function_call in response.function_calls:
                func_name = function_call.name or ""
                arguments = function_call.args or {}
                file_path = arguments.get("file_path") or arguments.get("directory") or ""
                content = arguments.get("content", "")
                args = arguments.get("args", "")
                func_response = call_func(func_name, file_path, content, args)
                print(f"Function call: {func_name} with arguments {arguments} \n response: {func_response}")
                history.append(types.Content(role="tool", parts=[types.Part.from_function_response(name=func_name, response={"result": func_response},)]))
        if response.text:
            print("AI response:", response.text)
        if response is None or response.usage_metadata is None:
            print("response is malformed")
            break
        
        #adding to history
        
    #print(history)


main()
