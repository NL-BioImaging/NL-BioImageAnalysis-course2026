# Principles of image segmentation with AI

In this session we segment cells and detect spots with pretrained deep learning models.
We do not train anything AI models ourselves, but we look at what
these models need from us in order to work.

The three notebooks follow the same shape: first an example image that suits the model,
then our own images, then a few exercises.

- `stardist.ipynb` — nuclei as star-convex shapes with StarDist
- `cellpose.ipynb` — cells and nuclei from predicted flows with Cellpose
- `spotiflow.ipynb` — spots as coordinates with Spotiflow, combined with the nuclei

Each notebook has a matching `*_answers.ipynb` with answers to the exercises.

## Learning goals

After these notebooks you can:

1. Run different pretrained deep learning models on your own images from Python, without
   training anything yourself.
2. Say what each of the three models predicts, and choose the one that fits your
   objects: outlines of nuclei (StarDist), outlines of cells of any shape (Cellpose),
   or positions of small spots (Spotiflow).
3. Recognise that the size of your objects, compared to the images the model was
   trained on, decides whether a pretrained model works, and set it with `scale`
   (StarDist) or `diameter` (Cellpose).
4. Explain why the input has to be normalized, and recognise what goes wrong when it
   is not.
5. Judge the result yourself: overlay the labels, count the objects, compare two
   methods, and check what you see before trusting the numbers.
6. Combine the output of two models into a measurement (foci per nucleus), and apply it
   to several images with a function and a loop.

## The data

The images are of cells that were either irradiated (`IR`) or left untreated
(`control`), fixed 2 hours later, and imaged in two channels: the DNA damage foci and
the nuclei. In the last notebook we count the foci per nucleus and compare the two
conditions.

## Requirements

- [Install](/preparation/preparation.md) JupyterLab and Conda
- A jlab environment, which we already installed on the first day.
    - `conda create -n jlab jupyterlab nb_conda_kernels`
- A dedicated deep learning environment:

```bash
conda create -n 2026_deep_learning -c conda-forge python=3.12 ipykernel nbformat numpy matplotlib tifffile scikit-image pandas seaborn pip
conda activate 2026_deep_learning
pip install "tensorflow>=2.16,<2.22" stardist "cellpose<4" spotiflow
```

The four deep learning packages come from `pip` rather than conda-forge: conda-forge
has no recent TensorFlow build for Windows, and no currently no Spotiflow package.

Notes:

- **Intel Macs**: TensorFlow has no macOS x86 wheels after 2.16.2, so use
  `pip install "tensorflow==2.16.2"` there.
- Everything in this session runs on the **CPU** in seconds to a minute per image. A
  GPU is not needed (and on Windows, pip-installed TensorFlow is CPU-only anyway).
- The first time you load a pretrained model it is downloaded, so you need an internet
  connection at the start of the session.

To start JupyterLab, use `conda activate jlab` and then `jupyter-lab`, and pick the
kernel **Python [conda env:2026_deep_learning]**.

## Files in `data/`

- `stardist_example1.tif` — example nuclei image from the StarDist training data
- `hela_cells.tif` — three-channel HeLa image used in the Cellpose notebook

## Files to download
- `MAX_2h_IR_*.tif`, `MAX_2h_control_*.tif` — two-channel images of irradiated and
  untreated cells (channel 0: DNA damage foci, channel 1: nuclei)
   Download from: https://surfdrive.surf.nl/s/qCSnzRnTZyA2Qqk
