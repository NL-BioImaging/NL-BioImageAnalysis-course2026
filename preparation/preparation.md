# Setting up your computer
So that we can fully utilise the time during the course, we ask that you prepare your computer before the course starts. Please follow the following steps and notify the course organisers if you get stuck. We can help, and would much rather do this prior to the course! 

## 1. Install git

You can check if you have Git installed by running `git config user.name`. This should return your name or user name. If not, install git. For installation of Git on either Linux, macOS or windows see here: https://git-scm.com/install/    
During this course you will use git to clone this repository, but git can do so much more! For a beginner's guide into using Git with GitHub, see https://swcarpentry.github.io/git-novice/index.html. Although this is a useful and well written guide, please note that GitHub (or any other cloud repository) is not required to use Git. For a complete reference to Git see https://git-scm.com/docs. 

## 2. Python and package managers
The Python ecosystem is diverse and dynamic. Each Python package is released with a version number, but it is not released in isolation! A package often *depends* on many packages, and, to ensure compatibility, the version numbers of these *dependencies* must be specified. These *Dependencies* are *dependent* on further *dependencies*... and you can see where this is going! Fortunately, there are many tools for organising a Python project and managing your Python packages, each with it's own pros and cons; some things even reducing down to personal preference. They all have at their core the concepts of *virtual environments* and *package management*. We will spend some time to cover the relevant parts of the Python ecosystem during the first lecture and there will be time to ask questions on this topic, so don't worry if these terms are unknown to you. For now, please install conda/miniforge from here: https://github.com/conda-forge/miniforge#install. Once you have Conda installed, you can create and manage isolated environments for each project you start or tool that you use, and conda will manage the packages for you. 
Conda is initialised during shell startup, therefore, **Before proceeding, you need a fresh shell.** Close your current shell and open a new one. If you see `(Base)` written in your shell, Conda is initialised and you are in the base environment.

## 3. Setup Jupyter lab
We will create a Conda environment and install Jupyterlab into it at the same time:  
`conda create -n jlab jupyterlab nb_conda_kernels`  
This creates an environment named jlab and installs jupyterlab and nb_conda_kernels into it. Notice how many *dependencies* this pulls. If required, you can also specifiy the version that you like to use. Now activate the jlab environment:  
`conda activate jlab` and run jupyterlab by typing `jupyter-lab`. The jupyter-lab command has many options and very useful features. If you are interested, type `jupyter-lab --help` to take a look. 
> Notice that we also installed nb_conda_kernels. This is an extremely useful python package (now a bit old-school?) that will discover iteractive python kernels and make them available to you in Jupyterlab.  
> If you create a notebook now in Jupyterlab, you will be able to select/start **Python [conda env:jlab]**. During the course you will create more conda environments, where you will install scientific packages for image analysis. Say, for example, you create a conda environment called 'day_1', where you install lots of python packages: If, (and only if!) you also install `ipykernel`, you will see **Python [conda env:day_1]** in this list .


## 4. Clone this repository
Now that Git, Conda and Jupyterlab are installed, you are ready to start this course! One final thing to do:

```
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026
cd NL-BioImageAnalysis-course2026
```
Good luck, and we hope that you enjoy the course. If you have any questions beforehand, please feel free to ask using the course registration email.




