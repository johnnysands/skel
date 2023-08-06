# Cookiecutter Python template

[`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable) package template.

## Usage

```bash
pip install cookiecutter
# local
cookiecutter path/to/repo/root
# https
cookiecutter https://github.com/johnnysands/skel
```

Answer the questions and you will have a new project directory.  Finish the setup:

```bash
cd PROJECT_SLUG
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -e '.[dev]'
git init
git add .
git commit -m "initial commit"

# full pre-commit hooks
pre-commit install
# push-only pre-commit hooks
pre-commit install --hook-type pre-push
```
