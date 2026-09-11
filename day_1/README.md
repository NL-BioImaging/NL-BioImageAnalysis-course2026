# Program

##  Morning: Introduction to Python and Jupyter notebooks

(..)

### Additional resources

(..)

##  Afternoon: Image processing concepts with Python

During this part, teaching will be done by live coding (inspired by [The Carpentries](https://carpentries.org/about-us/)).

This means the trainer will write and explain computer code, while
participants write along, such that they can immediately experience 
how the code works.

### Requirements

We'll make sure you're already set up during the morning session.
Below, for reference, you can find what you need for the afternoon session.

- [install](/preparation/preparation.md) JupyterLab and Conda
- A jlab environment
    - `conda create -n jlab jupyterlab nb_conda_kernels`
        - (*nb_conda_kernels* allows JupyterLab to connect to other environments)
- A dedicated image processing environment
    - `conda create -n 2026_image_processing -c conda-forge scikit-image scipy seaborn matplotlib tifffile numpy imageio pandas ipykernel nbformat`
        - (Here, *ipykernel* is required for the environment to be visible 
        in JupyterLab, *nbformat* is required to run one notebook from inside another notebook.)
- Example images
    - Copy the `images/` folder from `day_1/image_processing/images` to your
    local Jupyter notebook folder.

To start JupyterLab, first use the command `conda activate jlab` and then `jupyter-lab`.

### Content overview

There are three ±1 hour sessions this afternoon, with breaks in between. Topics that will be covered are:

- Part 1/3 (75 min)
    - Implement global and local **thresholding** to segment objects (with the histogram as important tool)
    - Understand what a **convolutional image operation** is, understand what the effect of a kernel is, and why to apply it.
    - Conceptually understand **morphology operations** (dilation, erosion, skeletonization)
    - Apply **common filters** (Gaussian, median, variance) and explain when each is appropriate
- Part 2/3 (60 min)
    - Understand when **background processing and correction** is important.    
    - Understand and use **masks, labels and regions** (connected components) to analyze ROIs in the image.
    - Perform **measurements** on the segmentations    
- Part 3/3 (60 min)
    - Build a simple **segmentation workflow** combining multiple steps
    - Evaluate segmentation quality through **visual inspection**


### Additional resources

- Bioimage notebooks: 
    - https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/intro.html
- Scipy and skimage documentation
    - https://scikit-image.org/docs/stable/user_guide/index.html
    - https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide
