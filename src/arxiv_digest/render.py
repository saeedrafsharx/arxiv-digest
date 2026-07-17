# src/arxiv_digest/fetch.py
from rich.table import Table
from rich.console import Console

console = Console()

def render_compact(papers):

    table = Table(title="Search result")

    table.add_column("ID")
    table.add_column("Title")
    table.add_column("Authors")
    table.add_column("Published")

    for paper in papers:
        table.add_row(paper.id, paper.title, paper.authors,
                       paper.published)
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
    md = "# Results\n\n"
    md += "| ID | Title | Authors | Published | Abstract | Link |\n"
    md += "|----|-------|---------|-----------|----------|------|\n"

    for paper in papers:
        md += (
            f"| {paper.id} "
            f"| {paper.title} "
            f"| {paper.authors} "
            f"| {paper.published} "
            f"| {paper.summary} "
            f"| {paper.link} "
        )

    with open(path, "w") as f:
        f.write(md)
    console.print(f"Results md file saved at: {path}")