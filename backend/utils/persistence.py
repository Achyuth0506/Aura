import json
from pathlib import Path

DATA_PATH = Path("data/state.json")

def save_state(state: dict):
    DATA_PATH.parent.mkdir(exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump(state, f, indent=2)

def load_state():
    if not DATA_PATH.exists():
        return {}
    with open(DATA_PATH) as f:
        return json.load(f)

