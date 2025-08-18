# Bon Sojourn AI Agent

A simple AI agent built with Google ADK that can answer queries and perform basic tasks.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

3. Test the agent configuration:
```bash
python3 main.py
```

## Usage

### Web Interface
Start the ADK web interface:
```bash
adk web
```
This will start a web server at `http://localhost:8080` where you can:
- Chat with the agent interactively
- See tool usage and responses
- Debug agent behavior

### Command Line Interface
Run the agent directly in the terminal:
```bash
adk run
```

### Features
The agent can:
- Answer general questions using OpenAI GPT-3.5-turbo
- Use tools like:
  - Get current time
  - Perform simple math calculations
  - Format JSON data

## Files

- `agent.py` - Main agent definition
- `tools.py` - Utility tools for the agent
- `main.py` - FastAPI web server entry point
- `requirements.txt` - Python dependencies
