import time
import json
import subprocess
from datetime import datetime

# Load task details
with open("Input/input.json", "r") as f:
    task_data = json.load(f)

# Sort tasks by fetch_time
tasks = sorted(task_data["tasks"], key=lambda x: datetime.strptime(x["fetch_time"], "%Y-%m-%d %H:%M:%S"))

for task in tasks:
    fetch_time = datetime.strptime(task["fetch_time"], "%Y-%m-%d %H:%M:%S")

    print(f"Waiting until {fetch_time} to fetch emails for Task {task['task_id']}...")

    while datetime.now() < fetch_time:
        time.sleep(10)

    print(f"Fetching emails for Task {task['task_id']} now...")
    subprocess.run(["python", "Bots/fetch_mails.py"])

    reply_now = input(f"Do you want to check and reply to emails for Task {task['task_id']} now? (yes/no): ").strip().lower()
    if reply_now == "yes":
        subprocess.run(["python", "Bots/reply_mails.py"])
