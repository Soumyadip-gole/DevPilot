# DevPilot


A terminal-based AI coding agent powered by Google Gemini. Give it a task in plain English and it will autonomously explore your codebase, read files, write code, and run scripts until the task is complete.

---

## How It Works

The agent runs an agentic loop — it keeps thinking and calling tools until it has fully completed your request, without needing any follow-up prompts from you.

```
User prompt
    ↓
Gemini decides which tool to call
    ↓
Tool executes → result fed back to Gemini
    ↓
Gemini continues reasoning (repeats as needed)
    ↓
Final response when task is done
```

At each step, the full conversation history (user messages, model responses, and tool results) is passed back to Gemini so it always has complete context of what has happened so far.

---

## Tools Available to the Agent

Gemini does not execute code directly. Instead, it is given a set of typed function declarations at startup. When Gemini decides a tool is needed, it returns a structured function call. The agent dispatches that call, runs the actual Python function, and feeds the result back into the conversation. This is what makes the loop agentic — Gemini is in control of what runs and when.

The four tools available to the agent are:

**`get_files_info`**  
Lists all files and subdirectories at a given path. The agent uses this to orient itself inside the working directory before reading or modifying anything — similar to running `ls` before touching a project.

**`get_files_content`**  
Reads and returns the full contents of a file. The agent calls this to understand existing code before making changes, so it never writes blindly.

**`write_file`**  
Creates a new file or overwrites an existing one with provided content. This is how the agent applies fixes, generates new scripts, or updates configuration files.

**`run_python_file`**  
Executes a Python script inside the working directory and returns its stdout and stderr output. The agent uses this to verify that code it has written actually runs correctly, closing the write → test loop autonomously.

---

## Working Directory

All file operations are scoped to a single working directory defined in the `.env` file via the `WORKING_DIRECTORY` variable. This serves two purposes:

**Security** — the agent cannot read or write outside the designated folder, so it has no access to the rest of your filesystem regardless of what it is asked to do.

**Scope definition** — by pointing `WORKING_DIRECTORY` at a specific project folder, you give the agent a clear context to work within. It knows that all paths it receives and all paths it generates are relative to that root, which prevents ambiguity across tool calls.

The working directory is injected at the function level inside `call_func.py` and is never exposed to the LLM directly. Gemini only ever sees and returns relative paths.

---

## Project Structure

```
Coding_agent/
├── main.py                        # Entry point, conversation loop, Gemini API calls
├── call_func.py                   # Dispatches tool calls, injects working directory
├── functions/
│   ├── get_files_info.py          # List files and directories
│   ├── get_files_contents.py      # Read file contents
│   ├── run_python_file.py         # Execute Python scripts, capture output
│   └── write_file.py              # Write or overwrite files
├── projects/                      # Default working directory for the agent
├── requirements.txt
└── .env
```

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/Soumyadip-gole/Coding_agent.git
cd Coding_agent
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Create a `.env` file in the root directory**

```
Gemini_api_key=your_gemini_api_key_here
WORKING_DIRECTORY=projects
```

Get a free Gemini API key at [aistudio.google.com](https://aistudio.google.com). You can point `WORKING_DIRECTORY` at any folder you want the agent to work inside.

**4. Run the agent**

```bash
python main.py
```

---

## Usage

Once running, type any coding task at the prompt:

```
input your prompt: fix the bug in calculator.py
```

The agent will explore the project, read the relevant files, apply the fix, and verify it by running the file — all on its own. Type `exit` to quit.

---
