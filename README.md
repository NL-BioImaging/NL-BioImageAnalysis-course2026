# NL-BioImageAnalysis-course 2026
Repository for the NL-BI Advanced Image Analysis course
21-24 September 2026, Erasmus MC, Rotterdam

## Getting started
```
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026.git
```

No Python/git installed? Check out the [preparations](preparation/preparation.md) page first!

## Jupyter book
To run the jupyter book locally

If you have cloned this repository locally you can use `uv` to install the dependencies to run Jupyter book locally.
Just run in the repository folder.`
Create a .venv based on `pyproject.toml`
```
uv sync
```

```
uv run jupyter book start
```