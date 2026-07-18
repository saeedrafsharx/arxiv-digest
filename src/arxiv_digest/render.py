# src/arxiv_digest/fetch.py
from rich.table import Table
from rich.console import Console

console = Console()

def render_compact(papers):

    table = Table(title="Search result", show_lines=True, highlight=True)

    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Authors")
    table.add_column("Published")

    for paper in papers:
        table.add_row(paper.id, paper.title, paper.authors,
                       paper.published)
        table.show_lines
    console.print(table)

def render_expanded(papers):
    
    table = Table(title="Search result")

    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Authors")
    table.add_column("Published")
    table.add_column("Abstract")
    table.add_column("Link")

    for paper in papers:
        table.add_row(paper.id, paper.title, paper.authors,
                       paper.published, paper.summary, paper.link)
    console.print(table)

def render_summary(papers):

    table = Table(title="Search result")

    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Authors")
    table.add_column("Published")
    table.add_column("Summary")

    for paper in papers:
        table.add_row(paper.id, paper.title, paper.authors,
                       paper.published, paper.ai_summary)
    console.print(table)

def render_markdown(papers, path) -> None:
    md = "# 📚 arXiv Digest\n\n"
    md += f"Found **{len(papers)} papers**.\n\n"

    for i, paper in enumerate(papers, 1):
        md += f"## {i}. {paper.title}\n\n"

        md += f"**Authors:** {paper.authors}\n\n"
        md += f"**Published:** {paper.published}\n\n"

        md += "### Abstract\n\n"
        md += f"{paper.summary}\n\n"

        md += f"🔗 [Paper Link]({paper.link})\n\n"

        md += "---\n\n"

    with open(path, "w") as f:
        f.write(md)

    console.print(f"Results file saved at: {path}")