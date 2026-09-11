# NL-BioImageAnalysis-course 2026
This repository contains the materials for the NL-BI Advanced Image Analysis course   

Organized from 21-24 September 2026 at Erasmus MC in Rotterdam

Course website: https://courses.microscopie.nl/?event_id=527

## Getting started
Check out hte preparation documentation for the course [here](preparation/preparation.md).
If you already have git and conda installed.

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
