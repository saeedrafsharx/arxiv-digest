from dataclasses import dataclass

@dataclass
class Paper:
    title: str
    authors: list[str]
    summary: str
    published: str
    link: str