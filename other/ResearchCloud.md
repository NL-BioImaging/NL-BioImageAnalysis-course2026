---
authors: [mpaul]
---

# Using SURF Research Cloud

[SURF Research Cloud](https://www.surf.nl/en/services/compute/surf-research-cloud) (SRC) lets you run a *workspace*: a virtual machine with a defined hardware configuration and tools preinstalled. For image analysis this means you can get a machine with an NVIDIA GPU, ready for AI-based tools, without installing anything yourself.

These instructions describe how to work on an existing workspace. If you want to learn how to create your own, see the [SRC documentation](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/9798172/SURF+Research+Cloud).

## 1. Access your workspace

- **You received a URL:** open it in your browser. You may be asked to log in with your account.
- **You did not receive a URL:** log in at <https://portal.live.surfresearchcloud.nl> and open your workspace from the dashboard.

An image analysis workspace comes in one of two flavours:

| Workspace | What you get | Use it for |
| --- | --- | --- |
| **Linux desktop** | A full Ubuntu desktop in your browser, with JupyterLab running on the same machine | GUI tools (napari, Cellpose, …) and notebooks |
| **Jupyter** | JupyterLab only, on a separate machine | Notebooks |

During the course we use the **Linux desktop**.

## 2. Linux desktop

The desktop opens in your browser via the link you received or from the portal. Here you can run GUI tools such as napari or Cellpose.

![Ubuntu desktop on SURF Research Cloud](images/desktop.png)

:::{tip}
To copy and paste text between your own computer and the desktop, press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Shift</kbd>. This opens a side menu with a clipboard.
:::

### Example: segment nuclei with StarDist in napari

1. Double-click the **Stardist** icon on the desktop. This opens napari with the stardist-napari plugin installed.
2. Open a sample image: `File → Open Sample → stardist-napari → Nuclei (2D)`.
3. Open the plugin: `Plugins → Stardist`.
4. Press **Run**. The segmentation appears as a new layer.

![StarDist segmentation in napari](images/napari-stardist.png)

:::{note}
For a smoother experience you could setup to connect with a Remote Desktop client instead of the browser (Windows: *Remote Desktop Connection*, Linux: *Remmina*). This requires a one-time password, see [Workspace access with TOTP](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/195854429/Workspace+access+with+TOTP#WorkspaceaccesswithTOTP-UbuntuDesktopwithTOTP).
:::

### Transfer data

1. **Course data** is already on the workspace. You don't need to copy anything in.
2. **To take your results home**, open the browser on the desktop and upload them to SURFdrive or a similar cloud storage service. Download them from there on your own computer.

Optional, if you want to set it up yourself:

3. Copy files over SFTP with [Cyberduck](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/112592488/Upload+data+to+a+workspace+with+Cyberduck).
4. [Connect Research Drive](https://servicedesk.surf.nl/wiki/display/WIKI/Connect+Research+Drive) as persistent storage on the workspace.

## 3. JupyterLab

Besides the desktop, you can also work in JupyterLab. It runs on the desktop workspace too, or on a separate Jupyter workspace. It works the same way in both cases.

- **Desktop workspace:** start JupyterLab from its icon on the desktop. It opens in the desktop's browser and runs inside the desktop.
- **Jupyter workspace:** JupyterLab opens directly in your own browser.

JupyterLab comes with several Python environments preinstalled, one per tool (biapy, cellpose, micro_sam, stardist, …). They show up as tiles in the **Launcher**.

![JupyterLab Launcher with the preinstalled environments](images/jupyter.png)

### Clone the repository

You can clone the course repository in two ways.

**Using the Git button.** Click the Git icon at the top of the file browser, paste the repository URL `https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026` and click *Clone*.

![Git clone button in the JupyterLab file browser](images/git_clone.png)

**Using a terminal.** Open a terminal via `File → New → Terminal`:

![Opening a terminal from the File menu](images/open_terminal.png)

Then run:

```bash
cd ~
git clone https://github.com/NL-BioImaging/NL-BioImageAnalysis-course2026
```

A folder `NL-BioImageAnalysis-course2026` now appears in the Jupyter file browser on the left (press the refresh button if it doesn't).

### Pick an environment

Open a notebook and select the environment (*kernel*) for the tool you want to use.

:::{image} images/jupyter-kernels.png
:alt: Selecting a kernel for a notebook
:width: 250px
:::

### Jupyter workspace only

The Launcher also has a **Desktop** tile, which opens the desktop in a new browser tab.

**Transfer data.** To copy files to the workspace, drag them onto the file browser or use the upload button (arrow icon) at the top of it. To copy a file back to your own computer, right-click it in the file browser and choose *Download*. This is convenient for small files.

### Install your own conda environment

The preinstalled environments cover the course. If you want your own, first enable conda in a terminal:

```bash
/etc/miniconda/bin/conda init
```

Open a new terminal, then create and activate an environment. Include `ipykernel` so JupyterLab can use it:

```bash
conda create -n my-env ipykernel
conda activate my-env
```

Install the packages you need, then register the environment as a kernel:

```bash
python -m ipykernel install --user --name my-env --display-name "My environment"
```

It now appears in the Launcher and in the kernel list.
