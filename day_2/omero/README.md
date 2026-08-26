
## Installation

### Conda
```
conda create -n nlbi26-day2-omero python=3.12
conda activate nlbi26-day2-omero

conda install zeroc-ice -y
pip install omero-py jupyterlab

```

### Alternative option: uv virtual environment 
#### Windows
```
uv venv --python 3.12
source .venv/bin/activate
uv pip install zeroc-ice@https://github.com/glencoesoftware/zeroc-ice-py-win-x86_64/releases/download/20240325/zeroc_ice-3.6.5-cp312-cp312-win_amd64.whl
uv pip install omero-py jupyterlab
```

#### Linux
```
uv venv --python 3.12
source .venv/bin/activate
uv pip install zeroc-ice@https://github.com/glencoesoftware/zeroc-ice-py-linux-x86_64/releases/download/20240202/zeroc_ice-3.6.5-cp312-cp312-manylinux_2_28_x86_64.whl
uv pip install omero-py jupyterlab
```


### Useful documentation
ezomero documentation - https://thejacksonlaboratory.github.io/ezomero/index.html

https://www.glencoesoftware.com/blog/2023/12/08/ice-binaries-for-omero.html
