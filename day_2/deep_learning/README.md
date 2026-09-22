# Deep learning for image analysis

In this session we segment cells and detect spots with pretrained deep learning models.
We do not train any AI models ourselves, but we look at how to use those in an image analysis workflow.

The three notebooks we use follow the same logic: first an example image that suits the model,
then our own images and a few exercises.

- `01_stardist.ipynb` — nuclei as star-convex shapes with StarDist
- `02_cellpose.ipynb` — cells and nuclei from predicted flows with Cellpose
- `03_spotiflow.ipynb` — spots as coordinates with Spotiflow, combined with the nuclei

Each notebook has a matching `_answers.ipynb` with answers to the exercises.

## Learning goals

After these notebooks you can:

1. Run different pretrained deep learning models on your own images from Python.
2. Say what each of the three models predicts, and choose the one that fits your
   objects: outlines of nuclei (StarDist), outlines of cells of any shape (Cellpose),
   or positions of small spots (Spotiflow).
3. Recognise that the size of your objects, compared to the images the model was
   trained on, decides whether a pretrained model works, and set it with `scale`
   (StarDist) or `diameter` (Cellpose).
4. Explain why the input has to be normalized, and recognise what goes wrong when it
   is not.
5. Combine the output of two models into a measurement (foci per nucleus), and apply it
   to several images with a function and a loop.

## Installation instructions

- [Install](/preparation/preparation.md) JupyterLab and Conda
- A jlab environment, which we already installed on the first day.
    - `conda create -n jlab jupyterlab nb_conda_kernels`
- A dedicated deep learning environment:

```bash
conda create -n 2026_deep_learning -c conda-forge python=3.12 ipykernel nbformat pip
```
```bash
conda activate 2026_deep_learning
```
```bash
pip install "tensorflow>=2.16,<2.22" stardist "cellpose<4" spotiflow numpy matplotlib tifffile scikit-image pandas colorcet
```

The deep learning packages come from `pip` rather than conda-forge: conda-forge
has no recent TensorFlow build for Windows, and currently no Spotiflow package.

Notes:

- **Intel Macs**: TensorFlow has no macOS x86 wheels after 2.16.2, so use
  `pip install "tensorflow==2.16.2"` there.
- Everything in this session runs on the **CPU** in seconds to a minute per image. A
  GPU is not needed (and on Windows, pip-installed TensorFlow is CPU-only anyway).
- The first time you load a pretrained model it is downloaded, so you need an internet
  connection at the start of the session.

To start JupyterLab, use `conda activate jlab` and then `jupyter-lab`, and pick the
kernel **Python [conda env:2026_deep_learning]**.

## The data

Apart from the example data we have several images of cells that were either irradiated (`IR`) or left untreated
(`control`), fixed 2 hours later, and imaged in two channels: the DNA damage foci and
the nuclei. In the last notebook we count the foci per nucleus and compare the two
conditions.

### Files in `data/`

- `stardist_example1.tif` — example nuclei image from the StarDist training data
- `hela_cells.tif` — three-channel HeLa image used in the Cellpose notebook

### Files to download
- `MAX_2h_IR_*.tif`, `MAX_2h_control_*.tif` — two-channel images of irradiated and
  untreated cells (channel 0: DNA damage foci, channel 1: nuclei)
   Download from: https://surfdrive.surf.nl/s/qCSnzRnTZyA2Qqk



## Running the notebooks

In your terminal go to the folder with the Github repository.

```
cd NL-BioImageAnalysis-course2026
```

Then activate the `jlab` environment.

```
conda activate jlab
jupyter lab
```

After jupyter lab has opened in your browser, go to `day_2/deep_learning` open the first notebook `01_stardist.ipynb`.
