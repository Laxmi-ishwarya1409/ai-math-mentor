import json, os
from datetime import datetime

MEMORY_FILE = "backend/memory/memory.json"

def save_to_memory(record):
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    record["timestamp"] = str(datetime.now())
    data.append(record)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def search_memory(problem_text):
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    matches = []
    for item in data:
        if problem_text.lower() in item["input"].lower():
            matches.append(item)

    return matches