---
authors: [mpaul]
---

# Setup SURF research cloud for image analysis

[SURF Research Cloud](https://www.surf.nl/en/services/compute/surf-research-cloud) is a service from SURF which allows to setup reproducible 'virtual machines' for your project, with the option to have different tools preinstalled and with defined hardware configuration. 
For example, it makes it easy to setup an environment with a Nvidia GPU to be used for AI-based image analysis applications. 
This environment can be a **Jupyter server** that is accessible from the browser with CUDA preinstalled, Or a **desktop environment** (Linux, Ubuntu) with different image analysis tools with GPU access.

The instructions below describe how to access an existing running machine. If you like to learn more on how to deploy new machines you can check more information here.

## Jupyter lab

If you received a URL to the Jupyter server you can access it directly. It might ask you to login with an account.
Otherwise you need to login with your account to https://portal.live.surfresearchcloud.nl 

The jupyter server already comes with some Python environments pre-installed.

### Clone the repository

![alt text](images/git_clone.png)

In **Jupyter** open a terminal, you can go to `File -> New -> Terminal`

Alternatively you can clone the repository via the terminal:

![alt text](images/open_terminal.png)

```
cd ~
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026
```

![alt text](images/jupyter.png)

You should now see a new folder on the right with the content of the repository (you might need to press the refresh button).

Now you can start working on a notebook.

![alt text](images/jupyter-kernels.png)

Depending on the tool you can pick the right Python environment that is already preinstalled.

### Installing own conda environments

If you like to install your own conda environments you need to enable conda.

- Open a Terminal in Jupyter
- Run:
```
/etc/miniconda/bin/conda init
```

- Now you should be able to run:

```
conda create -n <your-environment>
conda activate <your environment>
```
Install what you like, then add to the jupyter kernels.

```
python -m ipykernel install --user --name <name> --displayname <Friendly name>
```

## Linux desktop

For GUI tools (e.g. napari, cellpose) it is easier to deploy a full desktop. Within the desktop you can also run JupyterLab.

![alt text](images/desktop.png)

The desktop can be accessed via the browser (easiest).

::: {tip}
If you like to copy text from your own desktop to the machine or vice versa: `Ctrl-Alt-Shift` will open a menu on the side which allows you to copy and paste text.
:::

### Opening applications

In this example we will open napari with the Stardist plugin preinstalled.    
- Click on the Stardist icon on the desktop. It will open napari with the stardist-napari plugin installed.
- In napari you can try open a sample image via `File-> Open Sample -> stardist-napari -> Nuclei(2D)`
- Open the plugin `Plugins -> Stardist`
- Press `Run` and the segmentation should appear.

![alt text](images/napari-stardist.png)

::: {note}
For more convenience you can setup Remote Desktop (Windows: Remote Desktop Connection, Linux: Remmina)
Then to get access you need to use single use password - [link](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/195854429/Workspace+access+with+TOTP#WorkspaceaccesswithTOTP-UbuntuDesktopwithTOTP)
:::

## Transfer data
