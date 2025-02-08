- **Title:** Gmail Automation Bot

- **Description/Overview:**
The Gmail Automation Bot is a Python-based program that automates email fetching, logging, and response handling using the IMAP protocol. It allows users to schedule email retrieval tasks at specific times, stores email data in an organized format, and enables manual or automated replies.

- **Features:**
1. Scheduled Email Fetching – Users can specify a fetch time in input.json, and the bot will automatically retrieve unread emails at that time.
2. IMAP-Based Email Reading – The bot securely connects to Gmail's IMAP server to fetch emails.
3. Task-Based Execution – Each email-fetching task is assigned a unique Task ID, ensuring clear tracking and logging.
4. Structured Data Storage – Fetched emails (subject, sender, body, and timestamp) are stored in a single output.json file, making it easy to review past emails.
5. Manual Reply Handling – The bot does not auto-reply to all emails; instead, it asks for user confirmation before responding.
6. Secure Configuration – Authentication details like the App Password and IMAP settings are stored separately in config.json for security and easy modification.

- **Use Cases:**
1. Automate Inbox Monitoring – Retrieve and analyze incoming emails at scheduled times.
2. Organized Email Logging – Store fetched emails in a well-structured JSON format for easy retrieval.
3. Assist in Email Replies – Reduce manual effort by automating email response workflows.

- **What the bot exactly does:**
1. Waits until the scheduled fetch time
2. Connects to Gmail via IMAP
3. Fetches unread emails
4. Saves the emails in output.json
5. Asks for user confirmation before replying
6. Sends a reply if confirmed
7. Logs the reply in output.json

- **What It Will NOT Do:**
1. It will NOT auto-reply without confirmation.
2. It will NOT modify your emails in Gmail.
3. It will NOT delete or mark emails as read.

- **Dependencies to Install for Gmail Automation Bot:**

Before running the bot, you need to install the following Python libraries:

Run this command to install all required dependencies:

`pip install imapclient smtplib email json5 python-dotenv datetime time requests logging
`
- **Steps to Run the Gmail Automation Bot:**
1. Ensure All Dependencies Are Installed.
2. Set Up Your Gmail Account
- Enable IMAP in Gmail settings.
- Generate an App Password if 2FA is enabled.
3. Configure config.json and input.json
- Ensure config.json has correct credentials(valid gmail & password).
- Set fetch_time in input.json to a valid time.
4. Run the Program:
Make sure that you are in the root directory and run this command for execution:

`python -m Run.main
`

- **Expected Behavior:**
1. The bot waits until the scheduled time in input.json.
2. Fetches unread emails and stores them in output.json.
3. Asks you if you want to reply to any emails.
4. If user does not want to reply, it moves to the next mail.
5. If the user confirms and wants to send a reply, the content of the mail is feeded by the user and the bot sends a reply using reply_mails.py.

- **Expected Output**

For this input.json:

`{
    "tasks": [
        {
            "task_id": "TASK-IMMEDIATE",
            "fetch_time": "2025-01-28 19:09:00"
        },
        {
            "task_id": "TASK-IMMEDIATE",
            "fetch_time": "2025-01-28 19:42:00"
        }
    ]
}
`

The output.json will be created in the Output folder and have the mails accordingly. The sample file is shown as follows:

`{
    "tasks": [
        {
            "task_id": "TASK-IMMEDIATE",
            "fetched_at": "2025-01-28 19:09:07.387199",
            "emails": [
                {
                    "email_id": "369",
                    "subject": "Hello",
                    "sender": "Anish Salpe <anishsalpe42@gmail.com>",
                    "date": "Tue, 28 Jan 2025 19:07:32 +0530",
                    "body": "Hiiiass\r\n"
                }
            ]
        }`

- **Credits & Acknowledgments:**

This project was undertaken as part of my internship, where I developed a Gmail automation system using IMAP and SMTP to efficiently read, process, and respond to emails. I would like to express my sincere gratitude to **IoTIoT** for their invaluable guidance and support throughout the project. A special thanks to **Nikhil Bhaskaran**, Founder of IoTIoT, for his mentorship and insightful direction, which greatly contributed to the successful completion of this work. I also extend my appreciation to **Sneha Bhapkar** for her valuable support and assistance during the process.
