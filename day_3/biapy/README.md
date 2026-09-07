# BiaPy - accessible deep learning for bioimage analysis

## Lecture
Daniel Franco-Barranco (MRC Laboratory of Molecular Biology, Cambridge)

## Hands-on

### Google Colab
- Go to: https://biapyx.github.io/
- Select Colab notebooks
- Select `2D Instance Segmentation`
- Open Google Colab
Requires a Google account, login
- Install BiaPy (it might ask to restart session to install CUDA)
- At Manage File Sources pick `Option 3: Download an Example Dataset`

- Skip the OPTIONAL BioImage Model Zoo models check, it will take a long time to load

- Define parameters

-> Fix: biapy = BiaPy(f'/content/{job_name}.yaml', result_dir=output_path, name=job_name, run_id=1, gpu="0") (same issue at the inference cell lower)

biapy_config['TRAIN']['VERBOSE'] = True

- Start training


Try with low number of epochs first (e.g. 10 )
100 epochs takes ~23 min
Check the Loss and IoU curves and visualize results

## Inference notebook
Upload some image (with or without GT)

Model selection: Option 1

Run inference

Download the results

## Locally
```
conda create -n nlbi26-day3-biapy python=3.13
conda activate nlbi26-day3-biapy
pip install biapy
```