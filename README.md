# MWE for reproducing holoviews Issue 6086

This is a sample MWE for https://github.com/holoviz/holoviews/issues/6086

## Setup

Create virtual environment and install dependencies from requirements.txt

## Running

```
nbsite build --what=html --output=builtdocs --org holoviz --project-name holoviews
```

After first build, it is possible reproduce the problem also with

```
sphinx-build -b html doc/ builtdocs/ -a
```