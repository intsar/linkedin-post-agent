# LinkedIn Post Agent

This Python agent fetches LinkedIn post ideas from a Google Sheet and generates professional posts using either:
1. A local Ollama model (like Mistral)
2. OpenAI's ChatGPT API

## Columns expected in Google Sheet
- `idea`: Your LinkedIn post idea
- `status`: `pending` or `done`
- `post`: Optional column to store generated post

## Scheduled Run (optional) at 10 PM
Use `cron` or Task Scheduler to run daily at 10 PM.
- `ollama_agent.py` for local LLM
- `chatgpt_agent.py` for OpenAI API
  
## Manual Run
To run the script immediately (bypassing scheduled time), use the --now flag:
- python ollama_agent.py --now
 # OR
- python chatgpt_agent.py --now


Authentication Setup
1. Google Sheets Access
Go to Google Cloud Console -

Create a new project (if not already)

Enable Google Sheets API and Google Drive API

Go to APIs & Services > Credentials

Click Create Credentials > Service Account

Download the JSON key file and rename it to: google_creds.json

Share your Google Sheet with the service account email (e.g., your-service-name@project-id.iam.gserviceaccount.com) with Editor access.

2. OpenAI API Key
Go to https://platform.openai.com/account/api-keys

Generate a new API key

Set it as an environment variable or paste it inside the script as needed:

Requirements ( create virtual env before run this)
Install the dependencies using:
pip install -r requirements.txt

