# BiaPy - accessible deep learning for bioimage analysis

## Lecture
Daniel Franco-Barranco (MRC Laboratory of Molecular Biology, Cambridge)

## Hands-on session

### Google Colab
Yoou will need a Google account to run this. Alternatively you can follow 

#### 2D Instance Segmentation
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

## Run bia locally
```
conda create -n nlbi26-day3-biapy python=3.13
conda activate nlbi26-day3-biapy
pip install biapy
```