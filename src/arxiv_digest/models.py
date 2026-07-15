# src/arxiv_digest/models.py

from dataclasses import dataclass

@dataclass
class Paper:
    id: str
    title: str
    authors: str
    summary: str
    published: str
    link: str