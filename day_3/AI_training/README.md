# Preparing data, training and evaluating an AI model

Pretrained models such as StarDist and Cellpose work well when your images resemble the
data they were trained on. When your images look different, or you want to segment
specific objects that these generalist models aren't designed for, training your own model can
give better results.

In this tutorial we illustrate this by training a nuclei segmentation model on the
actin (phalloidin) channel instead of the DNA (Hoechst) channel. The motivation is that if
such a model works well, the DNA stain could potentially be left out from future
experiments, freeing up that channel for another marker.

There are different workflows for generating the training labels. Rather than manually
annotating nuclei by hand, we use StarDist to segment nuclei on the DAPI channel and use
these segmentations as ground truth labels paired with the corresponding phalloidin
images.

The training data is prepared in this notebook using public data from the Image Data
Resource:

- `data_collection_IDR_stardist.ipynb` — collect images from the Image Data Resource as
  remote OME-Zarr, generate nuclei labels with StarDist on the DAPI channel, check and
  correct them in napari, and write them to `training_data/`.

To save you time, we provide the training data directly, so you don't need to run this
notebook yourself and can focus on the training step.

Ideally, the training notebook is run on a computer with a GPU, reducing training time to a few
minutes and allowing you to explore the parameters relevant to training an optimal
model.

- `training_semantic.ipynb` — the main notebook for this session. 
  We will split `training_data/` into training and test sets, train a first model on the foreground only,
  read BiaPy's own curves and scores, then work out why touching nuclei end up merged, add
  the contour channel and compare the two runs.

- `training_cellpose.ipynb` — An alternative approach which fine-tunes the pretrained Cellpose-SAM model, 
and compared before and after.

## Training data 

Download data from: https://surfdrive.surf.nl/s/2pi8d9gzdBy8YTj

## Running on SURF Research Cloud

All environments are already installed on the workspaces. Clone this repository inside Jupyter lab
(see [Using SURF Research Cloud](/other/ResearchCloud.md)), open the notebook and pick the
matching kernel from the launcher (right top above notebook).

![alt text](images/image.png)

## Environments

To run the notebook locally it is best to use separate environments. 
All include `ipykernel` so JupyterLab can use them.

### `data_collection_IDR_stardist.ipynb`

```bash
conda create -n nlbi26-day3-prep -c conda-forge python=3.12 ipykernel
conda activate nlbi26-day3-prep
pip install "tensorflow>=2.16,<2.22" stardist requests zarr "dask[array]" ome-zarr \
    tifffile scikit-image matplotlib "napari[all]"
```

On Intel Macs, TensorFlow has no macOS x86 wheels after 2.16.2, so use
`pip install "tensorflow==2.16.2"` there.

### `training_semantic.ipynb`

In this environment we will install biapy. If you want to use it with a GPU,
you might need to 
```bash
conda create -n nlbi26-day3-biapy -c conda-forge python=3.13 biapy ipykernel
conda activate nlbi26-day3-biapy
```

You can check if the GPU is detected:

```bash
python -c 'import torch; print(torch.__version__)'
>>> 2.12.1
python -c 'import torch; print(torch.cuda.is_available())'
>>> True
```

Training on a CPU is slow. Use a GPU where you can see below.

### `training_cellpose.ipynb`

Cellpose 4 (Cellpose-SAM) require a specific version of PyTorch, so it needs its own environment too:

```bash
conda create -n nlbi26-day3-cellpose -c conda-forge python=3.12 ipykernel
conda activate nlbi26-day3-cellpose
pip install "cellpose>=4"
```

It reads the `dataset/` split that `training_semantic.ipynb` creates, so run that notebook
up to the end of section 2 first. Training CellPose 4 on a CPU is not realistic so you really need to do this on a system with a GPU.


