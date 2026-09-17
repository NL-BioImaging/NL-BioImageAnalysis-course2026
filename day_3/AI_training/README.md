# Preparing data, training and evaluating an AI model

Pretrained models such as StarDist and Cellpose work well when your images resemble the
data they were trained on. When your images look different, or you want to segment
objects that these generalist models aren't designed for, training your own model can
give better results.

In this tutorial we illustrate this by training a nuclei segmentation model on the
actin (phalloidin) channel instead of the DNA (Hoechst) channel. The motivation is that if
such a model works well, the DNA stain could potentially be dropped from future
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

To save time, we provide the training data directly, so you don't need to run this
notebook yourself and can focus on the training step.

Ideally, training is done on a computer with a GPU, reducing training time to a few
minutes and allowing you to explore the parameters relevant to training an optimal
model.

- `training.ipynb` — generic vs. specific models and what BiaPy can do; split
  `training_data/` into training, validation and test sets, train a model with BiaPy, and
  experiment with settings that affect training.
- `evaluation.ipynb` — run generic StarDist and Cellpose models on the test set, place
  the trained BiaPy model alongside them, and discuss metrics: object count, IoU,
  precision, recall, F1, and which metric suits which biological question.

## Training data layout

The preparation notebook saves one folder with matching file names

```
training_data/
├── images/   # phalloidin channel, the input for the network
└── labels/   # nuclei labels made with StarDist, the target
└
```

In the notebook

```
dataset/
├── train/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

The validation set is not a folder: BiaPy takes a fraction of the training images for it
(`DATA.VAL.SPLIT_TRAIN`).

## Environments

Three notebooks, three environments. All include `ipykernel` so JupyterLab can use them.

### `data_collection_IDR_stardist.ipynb`

```bash
conda create -n nlbi26-day3-prep -c conda-forge python=3.12 ipykernel
conda activate nlbi26-day3-prep
pip install "tensorflow>=2.16,<2.22" stardist requests zarr "dask[array]" ome-zarr \
    tifffile scikit-image matplotlib "napari[all]"
```

The deep learning packages come from `pip` rather than conda-forge for the same reason as
on day 2: conda-forge has no recent TensorFlow build for Windows.

On Intel Macs, TensorFlow has no macOS x86 wheels after 2.16.2, so use
`pip install "tensorflow==2.16.2"` there.

### `training_semantic.ipynb`

BiaPy pulls in PyTorch, so it gets its own environment:

```bash
conda create -n nlbi26-day3-biapy -c conda-forge python=3.13 ipykernel
conda activate nlbi26-day3-biapy
pip install biapy
```

Training on a CPU is slow. Use a GPU where you can — see below.

### `evaluation.ipynb`

Uses the day 2 deep learning environment as it is (StarDist and Cellpose 3):

```bash
conda activate 2026_deep_learning
```

It does not run BiaPy; it reads the test predictions BiaPy wrote to
`biapy_output/<job_name>/results/<job_name>_<run_id>/per_image_instances/`. These are only
written when a training run finishes with `TEST.ENABLE: True`.

## Running on SURF Research Cloud

All environments are already installed on the course workspaces. Clone this repository
(see [Using SURF Research Cloud](/other/ResearchCloud.md)), open the notebook and pick the
matching kernel from the Launcher.

napari needs the Linux desktop workspace rather than JupyterLab alone. For painting
labels, connecting with a Remote Desktop client is considerably smoother than the browser
desktop.
