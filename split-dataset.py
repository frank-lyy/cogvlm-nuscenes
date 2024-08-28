import os
import shutil

def find_all_files(path, suffix=".jpg"):
    target_files = []
    for cur_dir, _, files in os.walk(path, followlinks=True):
        for f in files:
            if f.endswith(suffix):
                target_files.append(os.path.join(cur_dir, f))
    print(f'find {len(target_files)} files...')
    return target_files

all_files = find_all_files('/content/images')
os.makedirs("images_split", exist_ok=True)
os.makedirs("images_split/train", exist_ok=True)
os.makedirs("images_split/valid", exist_ok=True)
os.makedirs("images_split/test", exist_ok=True)

import random
random.seed(2023)
random.shuffle(all_files)
train = all_files[:8000]
valid = all_files[8000:8000+500]
test = all_files[8000+500:8000+500+1500]

print("building train")
for file in train:
    shutil.move(file, os.path.join("images_split/train", file.split("/")[-1]))
print("building valid")
for file in valid:
    shutil.move(file, os.path.join("images_split/valid", file.split("/")[-1]))
print("building test")
for file in test:
    shutil.move(file, os.path.join("images_split/test", file.split("/")[-1]))
print("done")