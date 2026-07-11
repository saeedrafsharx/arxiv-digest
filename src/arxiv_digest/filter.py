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