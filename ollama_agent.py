import gspread
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import time
from datetime import datetime
import requests

def generate_post_with_ollama(idea):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": f"Create a professional LinkedIn post for this idea: {idea}",
            "stream": False
        }
    )
    if response.status_code == 200:
        return response.json().get("response", "").strip()
    return "⚠️ Failed to generate post."

def process_ideas():
    print(f"[{datetime.now()}] Running Ollama LinkedIn Post Agent...")

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("LinkedIn Ideas").sheet1
    rows = sheet.get_all_records()

    for idx, row in enumerate(rows, start=2):
        if row['status'].strip().lower() == 'pending':
            idea = row['idea']
            post = generate_post_with_ollama(idea)
            sheet.update_cell(idx, 3, post)
            sheet.update_cell(idx, 2, 'done')
            print(f"✅ Processed idea with Ollama: {idea}")
            break
    else:
        print("ℹ️ No pending ideas found.")

schedule.every().day.at("22:00").do(process_ideas)

print("🤖 Ollama LinkedIn Post Agent running... (Ctrl+C to stop)")
while True:
    schedule.run_pending()
    time.sleep(60)
