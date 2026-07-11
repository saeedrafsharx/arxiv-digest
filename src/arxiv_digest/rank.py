# src/arxiv_digest/rank.py

def score(paper: object, keywords: list) -> float:

    paper_score = 0
    for keyword in keywords:
        if keyword in paper.title:
            paper_score += 1
        elif keyword in paper.summary:
            paper_score += 0.5
    return paper_score

def rank(papers: list, keywords: list) -> list:

    return sorted(papers, key=lambda paper: score(paper, keywords), reverse=True)