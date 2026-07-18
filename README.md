# arxiv-digest

Turn the latest arXiv papers into a clean, readable digest you can scan in seconds.

## Example output

![Example output](./docs/demo.gif)

## Install

```bash
uv tool install .
```

## Config example

```toml
[arxiv_digest]
keywords = ["transformers", "reasoning"]
max_results = 10
```

## Summarize mode

Use `--summarize` to generate a short AI summary for each paper. That is the feature that makes the output feel especially useful and is often the biggest reason people star the project.
