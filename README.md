# README

[Copier](https://copier.readthedocs.io/) template for a simple Python projects

- Python project with `src` and `test` managed by `poetry`
- `notebooks` for Jupyter notebooks
- `Makefile` as task runner. See `make help`

## Prerequisites

- `pyenv`
- `poetry`
- `copier`

## Project Setup

```sh
$ copier copy gh:leoshimo/copier_python_template my_project
$ cd my_project
$ poetry install
```

## API Keys

Add `.env` with `SOME_API_KEY=API_KEY`. Then use `python-dotenv`:

```python
import os
from dotenv import load_dotenv
load_dotenv()
os.environ.get('SOME_API_KEY')
```

