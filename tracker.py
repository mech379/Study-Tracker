import json, sys
FILE = "sessions.json"

def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add(topic, minutes):
    data = load()
    data.append({"topic": topic, "minutes": int(minutes)})
    save(data)
    print(f"Added: {topic} ({minutes} min)")

def list_sessions():
    for s in load():
        print(f"- {s['topic']}: {s['minutes']} min")

def total():
    return sum(s["minutes"] for s in load())

if __name__ == "__main__":
    if len(sys.argv) >= 4 and sys.argv[1] == "add":
        add(sys.argv[2], sys.argv[3])
    elif len(sys.argv) >= 2 and sys.argv[1] == "list":
        list_sessions()
    elif len(sys.argv) >= 2 and sys.argv[1] == "total":
        print(f"Total: {total()} min")
    else:
        print("Usage: tracker.py add <topic> <minutes> | list | total")
