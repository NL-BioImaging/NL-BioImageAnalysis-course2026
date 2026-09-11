---
authors: [mpaul, clewis, bvdbroek]
---

# Setting up your computer
So that we can fully utilise the time during the course, we ask that you prepare your computer before the course starts. 

Please follow the following steps and notify the course organisers if you get stuck. We can help, and would much rather do this prior to the course! 

:::{important}
If you **already have any version of conda** on your laptop (from a previous course, project, or an Anaconda install), first go to [Checking your conda channel configuration](#conda-channels) below before starting step 3.
:::

## 1. Open a terminal (command line)

Almost every step below is run by typing commands into a **terminal** (also called a *command line*, *shell*, or *console*). If you have never used one, don't worry: for now you only need to know how to open it. We will tell you which command to run to get everything running. How you do that depends on your operating system.

::::{tab-set}

:::{tab-item} Windows
:sync: windows

- Press the <kbd>Windows</kbd> key, type `cmd`, and press <kbd>Enter</kbd>. This opens **Command Prompt**, which is all you need to get started. (**PowerShell**, or **Terminal** on Windows 11, work just as well if you prefer them.)

After you install Miniforge (step 3), a dedicated **Miniforge Prompt** also appears in the Start menu. You can use that one whenever you want to run `conda` commands, since a plain Command Prompt won't have `conda` available until you've run it once.
:::

:::{tab-item} macOS
:sync: macos

- Press <kbd>Cmd</kbd> + <kbd>Space</kbd> to open Spotlight, type `Terminal`, and press <kbd>Enter</kbd>.
- Or open **Finder → Applications → Utilities → Terminal**.

The default shell is `zsh`; that is fine for everything in this course.
:::

:::{tab-item} Linux
:sync: linux

- On most desktops (GNOME, Ubuntu) press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>.
- Or open your application menu and search for **Terminal** (sometimes called *Console* or *Konsole*).
:::

::::

Throughout these instructions, a block like the one below means "type this into your terminal and press <kbd>Enter</kbd>":

```bash
git --version
```

## 2. Install git

### What is Git and why do you need it?
During the course, and in research more generally, you will constantly be editing code: fixing a bug, tweaking a parameter, adding a new analysis step. Git is a *version control system*: it keeps a complete history of every change you make to your files, so you can see exactly what changed, when, and why, and step back to an earlier working version the moment something breaks. Even if you never touch a cloud service like GitHub, this makes Git worth having, it works like an infinitely capable "undo" combined with a lab notebook for your code. Git also lets you try out a new idea on a separate *branch* without putting your working analysis at risk, and it's the standard way researchers package, share and jointly develop code, which is exactly how you'll get the material for this course onto your own machine.

### Installing Git

You can check first whether git is already installed by running:

```bash
git --version
```

If this prints a version number (e.g. `git version 2.43.0`) you can skip to step 3. If you get a "command not found" error, install it as follows.

::::{tab-set}

:::{tab-item} Windows
:sync: windows

Download and run the installer from <https://git-scm.com/download/win>. Most defaults are fine; a few options are worth checking:

- **Choosing the default editor used by Git**: select *Use the Nano editor by default* (you may need to scroll up in the dropdown to find it). 
- **Adjusting the name of the initial branch in new repositories**: keep *Let Git decide*.
- **Adjusting your PATH environment**: select *Git from the command line and also from 3rd-party software* (the recommended option). This puts `git` on your PATH so it works from Command Prompt and PowerShell.

Accept the defaults on the remaining screens and click *Install*. 
:::

:::{tab-item} macOS
:sync: macos

Running `git --version` once will prompt you to install the **Command Line Tools** — accept and let it finish. Alternatively, if you use [Homebrew](https://brew.sh): `brew install git`.
:::

:::{tab-item} Linux
:sync: linux

Use your package manager:

```bash
sudo apt install git      # Debian / Ubuntu
sudo dnf install git      # Fedora
```
:::

::::

Finally, tell git who you are (this is recorded alongside any changes you make). Run the two commands below one at a time, replacing the text between the quotes with your own name and email address.

First your name:

```bash
git config --global user.name "Your Name"
```

Then your email address:

```bash
git config --global user.email "you@example.com"
```

Git can do far more than we use it for here — it is the standard tool for maintaining and collaborating on code. For a gentle introduction see the [Software Carpentry Git lesson](https://swcarpentry.github.io/git-novice/); the full reference is at <https://git-scm.com/docs>. For now you do not need an account on a hosting service such as GitHub to follow this course.

## 3. Python and package managers
The Python ecosystem is diverse and dynamic. Each Python package is released with a version number, but it is not released in isolation! A package often *depends* on many packages, and, to ensure compatibility, the version numbers of these *dependencies* must be specified. These *Dependencies* are *dependent* on further *dependencies*... and you can see where this is going! Fortunately, there are many tools for organising a Python project and managing your Python packages, each with it's own pros and cons; some things even reducing down to personal preference. They all have at their core the concepts of *virtual environments* and *package management*. We will spend some time to cover the relevant parts of the Python ecosystem during the first lecture and there will be time to ask questions on this topic, so don't worry if these terms are unknown to you.

For now, please install **Miniforge** (a minimal conda installer preconfigured for the conda-forge channel). Get the installer for your system from <https://conda-forge.org/download/>.

::::{tab-set}

:::{tab-item} Windows
:sync: windows

Download the `.exe` installer and run it, accepting the default options.
:::

:::{tab-item} macOS
:sync: macos

Download the `.sh` installer script (pick the one matching your chip: **arm64** for Apple Silicon, **x86_64** for older Intel Macs), then run it from your terminal:

```bash
bash ~/Downloads/Miniforge3-MacOSX-arm64.sh
```

Follow the prompts and accept when it offers to run `conda init`.
:::

:::{tab-item} Linux
:sync: linux

Download the `.sh` installer script, then run it from your terminal:

```bash
bash ~/Downloads/Miniforge3-Linux-x86_64.sh
```

Follow the prompts and accept when it offers to run `conda init`.
:::

::::

Once conda is installed, you can create and manage isolated Python environments for each project or tool you use, and conda will manage the packages for you.

Conda is initialised during shell startup, therefore, **before proceeding, you need a fresh shell.** Close your current terminal and open a new one. If you see `(base)` at the start of your prompt, conda is initialised and you are in the base environment. On `Windows` you can use **Miniforge Prompt** as there conda is for sure initialized.

## 4. Set up JupyterLab

Create a conda environment and install JupyterLab into it in one step:

```bash
conda create -n jlab jupyterlab nb_conda_kernels
```

This makes an environment named `jlab` and installs `jupyterlab` and `nb_conda_kernels` into it. Notice how many *dependencies* this pulls; press <kbd>y</kbd> when asked to confirm.

Now activate the environment 

```bash
conda activate jlab
```

Then start JupyterLab:
```
jupyter-lab
```



:::{tip}
`jupyter-lab` has many options and features. Run `jupyter-lab --help` to take a look.
:::

:::{note}
We also installed `nb_conda_kernels`. This package discovers Jupyter kernels from your other conda environments and makes them available in JupyterLab. When you create a notebook you will be able to select **Python [conda env:jlab]**.

During the course you will create more conda environments for scientific image-analysis packages. If (and only if) you also install `ipykernel` in such an environment — say one called `day_1` — it will show up here as **Python [conda env:day_1]**.
:::

:::{important} You are done for now!
Steps 1–4 are all you need to do before the course. Step 5 we will do together at the start of the course, because the course material is still being updated until then.

Good luck, and we hope that you enjoy the course. If you have any questions beforehand, please feel free to ask using the course registration email.
:::

## 5. Clone this repository (at the start of the course)

You don't need to do this step until the course starts, because the material is still being updated. At the start of the course we will do this together.

Cloning the repository downloads all its files into a folder on your computer.

A terminal is always "in" a folder, its *working directory*, and `git clone` downloads the repository into whatever folder you are in. Open a **fresh terminal** so you start in your home folder (`C:\Users\<you>` on Windows, `/Users/<you>` on macOS, `/home/<you>` on Linux), then run:

```bash
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026
cd NL-BioImageAnalysis-course2026
```

The first line creates a folder named `NL-BioImageAnalysis-course2026` in your home folder. The second, `cd` ("change directory"), moves the terminal into it, so the following commands act on the course material. You can check where you are at any time with `pwd` (macOS/Linux) or `cd` with no argument (Windows).

:::{tip}
To come back to the course material in a later session, open a terminal and `cd` into that folder again, for example `cd ~/NL-BioImageAnalysis-course2026`. 
:::

## Notes

(conda-channels)=
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
