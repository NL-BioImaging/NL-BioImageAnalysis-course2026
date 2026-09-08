

# Image processing

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

### The environment for Image processing fundamentals

For this afternoon, you'll need to install the following 
libraries as well:

```sh
# Environment 
conda create -n 2026_image_processing -c conda-forge scikit-image scipy seaborn matplotlib tifffile numpy imageio pandas ipykernel
```

*Note that ipykernel is required for the environment to be visible 
in jupyter-lab.*

### Using the envirnoment

To use JupyterLab and this environment, [as explained](https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026/blob/main/preparation/preparation.md), use:
```sh
conda activate jupyter-lab
jupyter-lab
```

### Example images

You'll need to download the example data folder located at:
`day_1/image_processing/images`.

## Contents overview

There are three ±1 hour sessions this afternoon, with breaks in between. Topics that will be covered are:

- Hour 1 (75 min)
    - Implement global and local **thresholding** to segment objects (with the histogram as important tool)
    - Understand and use **masks, labels and regions** (connected components) to analyze ROIs in the image.
    - Understand what a **convolutional image operation** is, understand what the effect of a kernel is, and why to apply it.
- Hour 2 (60 min)
    - Apply **common filters** (Gaussian, median, variance) and explain when each is appropriate
    - Conceptually understand **morphology operations** (dilation, erosion, skeletonization)
    - Understand when **background processing and correction** is important.
- Hour 3 (60 min)
    - Build a simple **segmentation workflow** combining multiple steps
    - Evaluate segmentation quality through **visual inspection**
    - Perform **measurements** on the segmentations





