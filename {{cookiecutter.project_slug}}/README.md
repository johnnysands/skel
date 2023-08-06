# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}


## Development

```bash
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

### Tests

Run `pytest`

