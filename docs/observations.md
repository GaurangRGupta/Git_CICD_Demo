# Experiment 2 observations

Solo run of Git, GitHub, and GitHub Actions for a tiny Python helper.

## Links

| Item | URL |
|---|---|
| GitHub repository | https://github.com/GaurangRGupta/Git_CICD_Demo |
| Pull Request | https://github.com/GaurangRGupta/Git_CICD_Demo/pull/1 |
| CI pass (workflow added) | https://github.com/GaurangRGupta/Git_CICD_Demo/actions/runs/38279650345 |
| CI fail (broken assertion) | https://github.com/GaurangRGupta/Git_CICD_Demo/actions/runs/38279728182 |
| CI pass (test restored) | https://github.com/GaurangRGupta/Git_CICD_Demo/actions/runs/38279796745 |

## Local commands used

```powershell
cd exp-2
uv sync
uv run python app.py
uv run pytest -v

git init          # already done; branch is main
git add app.py test_app.py requirements-dev.txt
git commit -m "Add prediction demo, tests, and uv pytest setup."
git remote add origin https://github.com/GaurangRGupta/Git_CICD_Demo.git
git push -u origin main

git switch -c feature-message
# edit app.py
git commit -m "Update prediction demo with a second sample output."
git push -u origin feature-message
# open and merge PR #1
git switch main
git pull origin main
```

`app.py` output after the feature-branch change:

```
MLOps Git/CI demo
Prediction: positive
Prediction: negative
```

Local tests: 2 passed.

## Commit history

```
* a7b8abd Restore the test so CI passes again.
* 21e2459 Break a test so CI can show a failing run.
* de559df Add Python CI workflow.
*   e55c147 Merge pull request: update prediction demo
|\
| * 3d229ce Update prediction demo with a second sample output.
|/
* 7816ffc Add prediction demo, tests, and uv pytest setup.
* 635fda6 Initial commit
```

## What was demonstrated

1. Git tracks each change as a commit (`add`, `commit`, `log`, `branch`, `switch`, `merge` via PR, `push`, `pull`).
2. GitHub hosts the shared copy: https://github.com/GaurangRGupta/Git_CICD_Demo
3. A feature branch (`feature-message`) was pushed and merged through Pull Request #1.
4. `.github/workflows/python-ci.yml` runs `pytest -v` on every push and pull request to `main`.
5. A broken assertion made CI fail; restoring the assertion made it pass again.

Jenkins was not used. GitHub Actions is the CI path in this experiment.

## Screenshot checklist (for the lab journal)

Take these from the browser/terminal before submitting:

- [ ] Terminal: `git log --oneline --decorate --graph --all`
- [ ] Terminal: `git branch -a` and `git remote -v`
- [ ] GitHub repo file list (`app.py`, `test_app.py`, `requirements-dev.txt`, `.github/workflows/python-ci.yml`)
- [ ] Pull Request #1 (merged)
- [ ] Actions: passing run `38279650345` or `38279796745`
- [ ] Actions: failing run `38279728182`
