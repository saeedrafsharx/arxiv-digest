# src/arxiv_digest/store.py
import json

def load_seen(path) -> set[str]:
    with open(path, "r") as f:
        seen_ids = json.load(f)
    print(f"Seen Ids loaded from {path}")
    return seen_ids

def save_seen(path, objects) -> None:

    ids = [obj.id for obj in objects]

    with open(path, "w") as f:
        json.dump(ids, f, indent=4)
    print(f"Ids saved to {path}")
