import os, shutil
from shutil import copyfile
from pathlib import Path
import glob

val_txt = "D:/2.dataset/coco/map/val.txt"
save_txt = "D:/2.dataset/coco/map/map.txt"

txt_path = "D:/2.dataset/coco/person_txt/"
out_txt_path = "D:/2.dataset/coco/map/txt/"

Path(out_txt_path).mkdir(parents=True, exist_ok=True)

def make_list():
    with open (val_txt, 'r') as f:
        lines = f.readlines()
    lines = list(map(lambda x: os.path.basename(x).rstrip().split(".")[0], lines))
    data = list(map(lambda x: x.rstrip(), lines))

    for i in data:
        copy_file = os.path.join(txt_path, i)+ '.txt'
        copyfile(copy_file, os.path.join(out_txt_path, i +'.txt'))



if __name__ == "__main__":
    make_list()
  