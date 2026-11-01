import json

def load():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)