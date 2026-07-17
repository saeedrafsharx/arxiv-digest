import feedparser
from .models import Paper
from typing import List

def parse_xml(raw_xml: str) -> List[Paper]:
    
    feed = feedparser.parse(raw_xml)
    papers = []

    for entry in feed.entries:
        paper = Paper(
            id=entry.get("id", "").strip(),
            title=entry.get("title", "").strip(),
            authors=str(entry.get("authors", "")).strip(),
            summary=entry.get("summary", entry.get("description", "")).strip(),
            published=entry.get("published", entry.get("updated", "")),
            link=entry.get("link", "").strip()
        )
        papers.append(paper)

    return papers