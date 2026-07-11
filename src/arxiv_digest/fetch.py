# src/arxiv_digest/fetch.py
import requests

BASE = "http://export.arxiv.org/api/query?search_query=all:"

def fetch(search_query: str, max_results: int = 10) -> str:
	
	url = f"{BASE}+{search_query}&start=0&max_results={max_results}"
	response = requests.get(url=url)
	return response.text

resp = fetch("autism")
from parse import parse_xml
parsd = parse_xml(resp)
print(parsd[1].title)
from filter import filter_papers
from config import import_config
conf = import_config()

filtrd = filter_papers(parsd, conf['keywords'])
print(len(filtrd))

from rank import rank
sortd=rank(filtrd,keywords=conf['keywords'])
print(sortd)