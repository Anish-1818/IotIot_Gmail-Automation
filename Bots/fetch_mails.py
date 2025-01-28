import imaplib
import email
import json
import os
from datetime import datetime

# Load config
with open("Config/config.json", "r") as f:
    config = json.load(f)

EMAIL = config["email"]
PASSWORD = config["app_password"]
IMAP_SERVER = config["imap_server"]
IMAP_PORT = config["imap_port"]

# Load task details
with open("Input/input.json", "r") as f:
    task_data = json.load(f)

# Load existing output.json
output_file = "Output/output.json"
if os.path.exists(output_file):
    with open(output_file, "r") as f:
        output_data = json.load(f)
else:
    output_data = {"tasks": []}

# Connect to IMAP
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

for task in task_data["tasks"]:
    task_id = task["task_id"]

    # Search for unread emails
    status, messages = mail.search(None, "UNSEEN")
    email_ids = messages[0].split()

    task_entry = {
        "task_id": task_id,
        "fetched_at": str(datetime.now()),
        "emails": []
    }

    for e_id in email_ids:
        _, msg_data = mail.fetch(e_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg["subject"]
                sender = msg["from"]
                date = msg["date"]

                # Extract email body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                task_entry["emails"].append({
                    "email_id": e_id.decode(),
                    "subject": subject,
                    "sender": sender,
                    "date": date,
                    "body": body
                })

    output_data["tasks"].append(task_entry)

# Save to output.json
with open(output_file, "w") as f:
    json.dump(output_data, f, indent=4)

print(f"Fetched emails for {len(task_data['tasks'])} tasks. Data saved to {output_file}.")

# Log activity
with open("Logs/botactivity.log", "a") as log_file:
    log_file.write(f"[{datetime.now()}] {len(task_data['tasks'])} tasks processed. Emails fetched.\n")

mail.logout()
