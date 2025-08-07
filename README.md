# LinkedIn Post Agent

This Python agent fetches LinkedIn post ideas from a Google Sheet and generates professional posts using either:
1. A local Ollama model (like Mistral)
2. OpenAI's ChatGPT API

## Columns expected in Google Sheet
- `idea`: Your LinkedIn post idea
- `status`: `pending` or `done`
- `post`: Optional column to store generated post

## Run the script
- `ollama_agent.py` for local LLM
- `chatgpt_agent.py` for OpenAI API

## Schedule (optional)
Use `cron` or Task Scheduler to run daily at 10 PM.
