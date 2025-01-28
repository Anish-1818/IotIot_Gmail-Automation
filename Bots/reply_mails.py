import smtplib
import json
import os
from email.mime.text import MIMEText
from datetime import datetime

# Load config
with open("Config/config.json", "r") as f:
    config = json.load(f)

EMAIL = config["email"]
PASSWORD = config["app_password"]

# Load fetched emails
output_file = "Output/output.json"
if not os.path.exists(output_file):
    print("No fetched emails found.")
    exit()

with open(output_file, "r") as f:
    data = json.load(f)

if not data["tasks"]:
    print("No unread emails to reply to.")
    exit()

for task in data["tasks"]:
    print(f"\nTask ID: {task['task_id']} | Fetched At: {task['fetched_at']}")
    
    for email_data in task["emails"]:
        print(f"\nEmail from: {email_data['sender']}")
        print(f"Subject: {email_data['subject']}")
        print(f"Body: {email_data['body'][:200]}...")  # Print first 200 chars
        user_input = input("Do you want to reply to this email? (yes/no): ").strip().lower()

        if user_input == "yes":
            reply_body = input("Enter your reply message: ")

            # Create email message
            msg = MIMEText(reply_body)
            msg["From"] = EMAIL
            msg["To"] = email_data["sender"]
            msg["Subject"] = f"Re: {email_data['subject']}"

            # Send email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL, PASSWORD)
                server.sendmail(EMAIL, email_data["sender"], msg.as_string())

            print("Reply sent successfully.")

            # Log activity
            with open("Logs/botactivity.log", "a") as log_file:
                log_file.write(f"[{datetime.now()}] Replied to {email_data['sender']} for Task {task['task_id']}.\n")

print("All emails processed.")
