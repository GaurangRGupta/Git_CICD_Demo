# Experiment 2: Git, GitHub and CI/CD

Tiny Python helper used to practice Git, GitHub, pull requests, and GitHub Actions.

`predict_label` returns `"positive"` when the score is at least 0.5, otherwise `"negative"`. That is enough to show a real test running in CI.

## Local setup (uv)

```powershell
cd exp-2
uv sync
uv run python app.py
uv run pytest -v
```

`requirements-dev.txt` lists `pytest` so the GitHub Actions workflow from the handout can install it with pip.

## GitHub

Remote repository name expected by the lab: `Git_CICD_Demo`.

Workflow file: [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml)

It runs on pushes and pull requests to `main`.
