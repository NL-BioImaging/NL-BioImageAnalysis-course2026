
# Using these notebooks in standalone


#### 

You should have a jlab environment (`conda create -n jlab jupyterlab nb_conda_kernels`, 
where *nb_conda_kernels* allows JupyterLab to connect to other environments).

#### Create an image processing environment

For this afternoon, we'll use the following environment:

```sh
# Environment 
conda create -n 2026_image_processing -c conda-forge scikit-image scipy seaborn matplotlib tifffile numpy imageio pandas ipykernel nbformat
```

Here, *ipykernel* is required for the environment to be visible 
in JupyterLab, *nbformat* is required to run one notebook from inside another notebook.


#### Copy example images

You'll need to use the example data folder located in the workshop repository at 
`day_1/image_processing/images`. 
You cloned (copied) this repository already to your local computer.

Copy the `images` folder to the folder where you are working on your Jupyter notebook.





