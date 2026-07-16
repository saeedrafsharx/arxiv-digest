# src/arxiv_digest/filter.py

def matches(paper: dict, keywords:list) -> bool:
    stat = False
    for key in keywords:
        if key in paper.title or paper.summary:
            stat = True
    return stat


def filter_papers(papers: list, keywords: list) -> list:

    papers_filtered = []
    for paper in papers:
        if matches(paper=paper, keywords=keywords) == True:
            papers_filtered.append(paper)
    return papers_filtered

def check_seen(paper: dict, ids:list) -> bool:
    
    seen = False
    for id in ids:
        if id in paper.id:
            seen = True
    return seen

def drop_seen(papers: list, ids: list) -> list:

    new_papers = []
    for paper in papers:
        if check_seen(paper=paper, ids=ids) == True:
            new_papers.append(paper)
    return new_papers