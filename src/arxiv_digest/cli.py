# src/arxiv_digest/cli.py
import argparse
from arxiv_digest.fetch import fetch
from arxiv_digest.filter import filter_papers, drop_seen
from arxiv_digest.parse import parse_xml
from arxiv_digest.rank import rank
from arxiv_digest.store import save_seen, load_seen
from pathlib import Path
from arxiv_digest.render import render_compact, render_expanded, render_markdown, render_summary
from arxiv_digest.summarize import summarize_papers

def build_parser():
    parser = argparse.ArgumentParser(
        prog="arxiv-digest",
        description="Get arxiv papers in a gist"
    )

    parser.add_argument(
        "query",
        help="Topic to search"
    )

    parser.add_argument(
        "--new",
        help="Only not seen results"
    )
    parser.add_argument(
        "--category",
        help="Define category of papers"
    )
    parser.add_argument(
        "--max",
        help="Maximum number of results to fetch"
    )
    parser.add_argument(
        "--since",
        help="Limit paper published time"
    )
    parser.add_argument(
        "--markdown"
    )
    parser.add_argument(
        "--summarize",
        help="Get the summary of the papers"
    )
    parser.add_argument(
        "--expand"
    )

    return parser

def main(args=None):

    args = build_parser().parse_args(args)
    file_path = Path("search_history.json")

    inital = fetch(search_query=args.query, max_results=args.max)
    parsed = parse_xml(raw_xml=inital)
    filtered = filter_papers(papers=parsed, keywords=args.query)
    ranked = rank(papers=filtered, keywords=args.query)

    if args.new:
        if file_path.is_file():
            ids = load_seen(file_path)
            ranked = drop_seen(ranked, ids)
        else:
            print("No previous search history found!")    
            pass
    
    if args.markdown:
        render_markdown(papers=ranked, path="results.md")
    elif args.expand:
        render_expanded(papers=ranked)
    elif args.summarize:
        summarized = summarize_papers(ranked)
        render_summary(papers=summarized)
    else:
        render_compact(papers=ranked)

if __name__ == "__main__":
    main()