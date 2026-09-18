# BiaPy - accessible deep learning for bioimage analysis

## Lecture
Daniel Franco-Barranco (MRC Laboratory of Molecular Biology, Cambridge)

## Hands-on session

### Google Colab
You will need a Google account to run this notebooks. Alternatively you can make use of Research Cloud.

#### Run 2D Instance Segmentation notebook
- Go to: https://biapyx.github.io/
- Select Colab notebooks
- Select `2D Instance Segmentation`
- Open Google Colab, login with your Google account
- Install BiaPy (it might ask to restart session to install CUDA)
- At Manage File Sources pick `Option 3: Download an Example Dataset`

- Skip the OPTIONAL BioImage Model Zoo models check, it will take a long time to load

- Define parameters

-> Fix: `biapy = BiaPy(f'/content/{job_name}.yaml', result_dir=output_path, name=job_name, run_id=1, gpu="0") (same issue at the inference nb lower)`

biapy_config['TRAIN']['VERBOSE'] = True

- Start training

- Check the results of the training
Try run the training with a low number of epochs first (e.g. 10 )
Check the Loss and IoU curves and visualize results

Run with a larger number of epochs, check if the results look better.

- Download model and configuration

#### Inference notebook
If you now like to use your model on other data you can use a different notebook:
- Upload some image (with or without GT)
- Model selection: Option 1
- Run inference
- Download the results

## Run on SURF research cloud
Alternatively you can use biapy on Research Cloud.
Access one on the desktops.
Open JuyterLab

A biapy notebook that works on SRC can be found in this repository.
Clone and select the biapy kernel.

## Run biapy locally
```bash
conda create -n nlbi26-day3-biapy python=3.13
conda activate nlbi26-day3-biapy
pip install biapy pyyaml
```