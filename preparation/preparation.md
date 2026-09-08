---
authors: [mpaul, clewis]
---

# Setting up your computer
So that we can fully utilise the time during the course, we ask that you prepare your computer before the course starts. Please follow the following steps and notify the course organisers if you get stuck. We can help, and would much rather do this prior to the course! 

## 1. Install git

### What is Git and why do you need it?
During the course, and in research more generally, you will constantly be editing code: fixing a bug, tweaking a parameter, adding a new analysis step. Git is a *version control system*: it keeps a complete history of every change you make to your files, so you can see exactly what changed, when, and why, and step back to an earlier working version the moment something breaks. Even if you never touch a cloud service like GitHub, this makes Git worth having, it works like an infinitely capable "undo" combined with a lab notebook for your code. Git also lets you try out a new idea on a separate *branch* without putting your working analysis at risk, and it's the standard way researchers package, share and jointly develop code, which is exactly how you'll get the material for this course onto your own machine.

You can check if you have Git installed by running `git config user.name` in a terminal or command prompt (in Windows: `Windows key` + `R`, type `cmd`). This should return your name or user name. If not, install git. For installation of Git on either Linux, macOS or windows see here: https://git-scm.com/install/.
For documentation and videos on Git, see https://git-scm.com/learn.

During this course you will use git to clone this repository, but git can do so much more! For a beginner's guide into using Git with GitHub, see https://swcarpentry.github.io/git-novice/index.html. Although this is a useful and well written guide, please note that GitHub (or any other cloud repository) is not required to use Git. For a complete reference to Git see https://git-scm.com/docs.

## 2. Python and package managers
The Python ecosystem is diverse and dynamic. Each Python package is released with a version number, but it is not released in isolation! A package often *depends* on many packages, and, to ensure compatibility, the version numbers of these *dependencies* must be specified. These *Dependencies* are *dependent* on further *dependencies*... and you can see where this is going! Fortunately, there are many tools for organising a Python project and managing your Python packages, each with it's own pros and cons; some things even reducing down to personal preference. They all have at their core the concepts of *virtual environments* and *package management*. We will spend some time to cover the relevant parts of the Python ecosystem during the first lecture and there will be time to ask questions on this topic, so don't worry if these terms are unknown to you. For now, please install conda/miniforge from here: https://github.com/conda-forge/miniforge#install. Once you have Conda installed, you can create and manage isolated environments for each project you start or tool that you use, and conda will manage the packages for you. 
Conda is initialised during shell startup, therefore, **Before proceeding, you need a fresh shell.** Close your current shell and open a new one. (In Windows: open the shell via Start (`Windows key`) -> Miniforge Prompt). If you see `(Base)` written in your shell, Conda is initialised and you are in the base environment.

## 3. Setup Jupyter lab
We will create a Conda environment named `jlab` and install Jupyterlab into it at the same time.
Type `conda create -n jlab jupyterlab nb_conda_kernels`  
This creates an environment named jlab and installs jupyterlab and nb_conda_kernels into it. Notice how many *dependencies* this pulls. If required, you can also specifiy the version that you like to use. Now activate the jlab environment:  
`conda activate jlab` and run jupyterlab by typing `jupyter-lab`. This will open a browser window with JupyterLab. The jupyter-lab command has many options and very useful features. If you are interested, type `jupyter-lab --help` to take a look. 
> Notice that we also installed nb_conda_kernels. This is an extremely useful python package (now a bit old-school?) that will discover iteractive python kernels and make them available to you in Jupyterlab.  
> If you create a notebook now in Jupyterlab, you will be able to select/start **Python [conda env:jlab]**. During the course you will create more conda environments, where you will install scientific packages for image analysis. Say, for example, you create a conda environment called 'day_1', where you install lots of python packages: If, (and only if!) you also install `ipykernel`, you will see **Python [conda env:day_1]** in this list .


## 4. Clone this repository
Now that Git, Conda and Jupyterlab are installed, you are ready to start this course! One final thing to do:

```
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026
cd NL-BioImageAnalysis-course2026
```
Good luck, and we hope that you enjoy the course. If you have any questions beforehand, please feel free to ask using the course registration email.


## Notes

### Checking your conda channel configuration

If you already have conda installed on your laptop (from a previous course, project, or Anaconda install), it's important to check that it's using the **conda-forge** channel and not the **defaults** channel. When accidentally pulling packages from `defaults`  you can run into Anaconda's Terms of Service for the `defaults` channel in some institutional/commercial contexts.

If you installed via **Miniforge** as instructed, you should already be safe. Miniforge ships preconfigured to use conda-forge only. But it's worth verifying, especially if you have an older conda install lying around.

**1. Check your current channels:**

```bash
conda config --show channels
```

This should return:

```
channels:
  - conda-forge
```

If instead you see `defaults` listed (alone or alongside `conda-forge`), you need to fix your configuration.

**2. Fix it:**

```bash
conda config --add channels conda-forge
conda config --set channel_priority strict
conda config --remove channels defaults
```

- The first line makes sure `conda-forge` is set and given top priority.
- The second line (`strict`) makes sure conda always prefers conda-forge packages over any other channel, even if one sneaks back in later.
- The third line removes `defaults` explicitly. If it wasn't there to begin with, this command will show a harmless error — that's fine, it just means there was nothing to remove.

**3. Verify the fix:**

```bash
conda config --show channels
```

You should now see only:

```
channels:
  - conda-forge
```
