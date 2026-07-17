# src/arxiv_digest/store.py
import json

def load_seen(path) -> set[str]:
    with open(path, "r") as f:
        seen_ids = json.load(f)
    return seen_ids

def save_seen(papers: list, path) -> None:

    ids = [paper.id for paper in papers]

    with open(path, "w") as f:
        json.dump(ids, f, indent=4)