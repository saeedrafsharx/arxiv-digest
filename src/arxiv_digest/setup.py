# src/arxiv_digest/setup.py

import shutil
import subprocess

MODEL = "gemma3:1b"

import requests


def ollama_running():

    try:
        requests.get(
            "http://localhost:11434/api/tags",
            timeout=2
        )
        return True

    except requests.exceptions.RequestException:
        return False

def setup_llm():

    if shutil.which("ollama") is None:
        raise RuntimeError(
            "Ollama is not installed.\n"
            "Visit https://ollama.com/download"
        )
    if not ollama_running():
        print("Starting Ollama...")

        subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        print(f"Downloading {MODEL}...")

        subprocess.run(
            ["ollama", "pull", MODEL],
            check=True
        )

        print("Setup complete!")
    else:
        print("Ollama is up and running!")