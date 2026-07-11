# src/arxiv_digest/fetch.py
import requests

BASE = "http://export.arxiv.org/api/query?search_query=all:"

def fetch(search_query: str, max_results: int = 10) -> str:
	
	url = f"{BASE}+{search_query}&start=0&max_results={max_results}"
	response = requests.get(url=url)
	return response.text
