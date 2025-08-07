import gspread
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import time
from datetime import datetime
import openai
import sys

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_post_with_chatgpt(idea):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a professional LinkedIn content creator."},
            {"role": "user", "content": f"Create a detailed LinkedIn post for: {idea}"}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def process_ideas():
    print(f"[{datetime.now()}] Running ChatGPT LinkedIn Post Agent...")

    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("LinkedIn Ideas").sheet1
    rows = sheet.get_all_records()

    for idx, row in enumerate(rows, start=2):
        if row['status'].strip().lower() == 'pending':
            idea = row['idea']
            post = generate_post_with_chatgpt(idea)
            sheet.update_cell(idx, 3, post)
            sheet.update_cell(idx, 2, 'done')
            print(f"✅ Processed idea with ChatGPT: {idea}")
            break
    else:
        print("ℹ️ No pending ideas found.")

# Check if manually triggered
if "--now" in sys.argv:
    process_ideas()
    sys.exit(0)  # Exit after one run
    
schedule.every().day.at("22:00").do(process_ideas)

print("🤖 ChatGPT LinkedIn Post Agent running... (Ctrl+C to stop)")
while True:
    schedule.run_pending()
    time.sleep(60)
