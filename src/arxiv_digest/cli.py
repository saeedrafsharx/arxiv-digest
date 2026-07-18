# src/arxiv_digest/cli.py
import argparse
from pathlib import Path
from arxiv_digest.rank import rank
from arxiv_digest.fetch import fetch
from arxiv_digest.parse import parse_xml
from arxiv_digest.setup import setup_llm
from arxiv_digest.store import save_seen, load_seen
from arxiv_digest.summarize import summarize_papers
from arxiv_digest.filter import filter_papers, drop_seen
from arxiv_digest.render import render_compact, render_expanded, render_markdown, render_summary

def build_parser():

    parser = argparse.ArgumentParser(
        prog="arxiv-digest",
        description="Get arxiv papers in a gist"
    )

    subparser = parser.add_subparsers(dest="command", required=True)

    subparser.add_parser(
        "setup",
        help="Install and configure the LLM"
    )

    search = subparser.add_parser(
        "search",
        help="Search ArXiv"
    )

    search.add_argument(
        "query",
        help="Topic to search"
    )
    search.add_argument(
        "--new",
        help="Only not seen results"
    )
    search.add_argument(
        "--category",
        help="Define category of papers"
    )
    search.add_argument(
        "--max",
        help="Maximum number of results to fetch"
    )
    search.add_argument(
        "--since",
        help="Limit paper published time"
    )
    search.add_argument(
        "--markdown",
        help="Save search results as an md file"
    )
    search.add_argument(
        "--summarize",
        help="Get the summary of the papers"
    )
    search.add_argument(
        "--expand",
        help="Get full paper abstract"
    )

    return parser

def main(args=None):

    try:
        args = build_parser().parse_args(args)
        file_path = Path("search_history.json")

        if args.command == "setup":
            return setup_llm()

        if args.command == "search":

            inital = fetch(search_query=args.query,max_results=10)
            
            parsed = parse_xml(raw_xml=inital)

            filtered = filter_papers(papers=parsed,keywords=args.query)

            ranked = rank(papers=filtered,keywords=args.query)

            if args.new:
                if file_path.is_file():
                    ids = load_seen(file_path)
                    ranked = drop_seen(ranked, ids)
                else:
                    print("No previous search history found!")    
            
            if args.markdown:
                render_markdown(papers=ranked,
                                 path=args.markdown)
            elif args.expand:
                render_expanded(papers=ranked)

            elif args.summarize:
                summarized = summarize_papers(ranked)
                render_summary(papers=summarized
                               )

            else:
                render_compact(papers=ranked)

            save_seen(papers=ranked, path="history.json")
            return 0
        
    except Exception:
        print("Could not Fetch")

if __name__ == "__main__":
    raise SystemExit(main())