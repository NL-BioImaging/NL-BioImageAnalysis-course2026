"""Split training_data/ into dataset/{train,val,test}/{images,labels}.

Backup for the exercise in 01_training_instance_segmentation.ipynb.
Run it from this folder: python organize_data.py
"""
from pathlib import Path
import random
import shutil

from skimage.io import imread

DATA = Path('training_data')
DATASET = Path('dataset')
VAL_FRACTION = 0.2
TEST_FRACTION = 0.2

# Images without nuclei teach the network nothing, so leave them out
ids = [f.stem for f in sorted((DATA / 'labels').glob('*.tif')) if imread(f).max() > 0]

random.seed(42)  # fixed, so everyone gets the same split
random.shuffle(ids)

n_test = round(len(ids) * TEST_FRACTION)
n_val = round(len(ids) * VAL_FRACTION)
splits = {
    'test': ids[:n_test],
    'val': ids[n_test:n_test + n_val],
    'train': ids[n_test + n_val:],
}

# Start from an empty folder, so no image from an earlier split stays behind
if DATASET.exists():
    shutil.rmtree(DATASET)

for split, split_ids in splits.items():
    for kind in ('images', 'labels'):
        folder = DATASET / split / kind
        folder.mkdir(parents=True)
        for image_id in split_ids:
            shutil.copy(DATA / kind / f'{image_id}.tif', folder / f'{image_id}.tif')
    print(f'{split}: {len(split_ids)} images')
