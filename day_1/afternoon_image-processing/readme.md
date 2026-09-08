

# Afternoon session

## Setup

### JupyterLab according to course instructions

During the preparation and morning session [you have already installed](https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026/blob/main/preparation/preparation.md) 
JupyterLab and Conda.

I called my `jlab` environment `2026_jlab`, but you should already be 
have a similar environment like this:

```sh
# Conda env with JupyterLab
conda create -n 2026_jlab jupyterlab nb_conda_kernels
```

Note that `nb_conda_kernels` allows JupyterLab to work with other environments than the one it's installed in.

### The environment for Image processing methods

The environment that holds all the libraries to follow
the "Image processing methods" part of the course, 
looks as follows:

```sh
# Environment 
conda create -n 2026_image_processing -c conda-forge scikit-image scipy seaborn matplotlib tifffile numpy imageio pandas ipykernel
```

*Note that ipykernel is required for the environment to be visible 
in jupyter-lab.*

### Using the envirnoment

To use JupyterLab and this environment, [as explained](), use:
```sh
conda activate jupyter-lab
jupyter-lab
```





