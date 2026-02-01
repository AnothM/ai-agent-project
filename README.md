# AI Agent Project

An educational AI coding agent built as part of the [Boot.dev AI Agent course](https://boot.dev). This project demonstrates how to build an LLM-powered agent that can interact with files and execute code.

## ⚠️ Security Warning

This is an **educational project** and is **not production-ready**.

**Do not use this agent on:**
- Production codebases
- Important projects
- Systems with sensitive data

**Why?**
- No sandboxing or security restrictions
- Unrestricted file system access
- Arbitrary code execution
- No rollback mechanisms
- LLM behavior can be unpredictable

This agent is intended for learning purposes only in isolated, controlled environments.

## Features

- File system operations (read, write, list)
- Python code execution
- LLM-powered decision making
- Function calling with Gemini API

## Setup

1. **Clone the repository**
   git clone <your-repo-url>
   cd ai_agent

2. Create a .env file with your API key:
    GEMINI_API_KEY=your_actual_api_key_here

3. Install dependencies
    uv sync

4. Activate the virtual environment
    source .venv/bin/activate

## Usage

Run the agent with a prompt:

uv run main.py "your prompt here"

Add --verbose for detailed output:

uv run main.py "your prompt here" --verbose

### Calculator Demo

This project includes a sample calculator application that the agent can interact with and fix.

**Run the calculator:**
uv run calculator/main.py "3 + 7 * 2"


## Deactivate Environment
When you're done:
 deactivate

