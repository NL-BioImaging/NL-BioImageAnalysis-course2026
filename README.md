# NL-BioImageAnalysis-course 2026
This repository contains the training materials for the NL-BI Advanced Image Analysis course   

Organized from 21-24 September 2026 at Erasmus MC in Rotterdam

Course website: https://courses.microscopie.nl/?event_id=527

The materials can be read as Jupyter book at:
https://nl-bioimaging.github.io/NL-BioImageAnalysis-course2026/

## Getting started
Check out the preparation documentation for the course [here](preparation/preparation.md).
If you already have git and conda installed.

```
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026.git
```

No Python/git installed? Check out the [preparations](preparation/preparation.md) page first!


## Jupyter book
It is possible to build the jupyter book locally. If you have cloned this repository you can use `uv` to install the dependencies to run Jupyter book. Don't have `uv` yet? See the [uv installation page](https://docs.astral.sh/uv/getting-started/installation/).
Just run in the repository folder.`
Create a .venv based on `pyproject.toml`
```
uv sync
```

```
uv run jupyter book start
```

## License
The course content (text, notebooks, images) in this repository is licensed as [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) by the contributors of this repository unless mentioned otherwise.
Code (scripts, code cells) is licensed under the [BSD 3-Clause License](LICENSE-CODE).