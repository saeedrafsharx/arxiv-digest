# src/arxiv_digest/cli.py
from ollama import chat

def summarize(paper: object, model: str = "gemma3:1b") -> str:
    try:
        prompt = f"""
    Summarize this scientific paper.

    Requirements:
    - Maximum two sentences.
    - Maximum 50 words.
    - Focus only on the main contribution and findings.
    - Do not include introductory phrases.

    Title:
    {paper.title}

    Abstract:
    {paper.summary}
    """
        response = chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        return response["message"]["content"]
    except Exception:
        return "Summary unavailable."

def summarize_papers(papers: list, model: str="gemma3:1b") -> list:

    for paper in papers:
        paper.ai_summary= summarize(
            paper,
            model=model
        )

    return papers
