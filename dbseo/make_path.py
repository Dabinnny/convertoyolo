import glob
import os
from shutil import copyfile
from pathlib import Path
from sklearn.model_selection import train_test_split

def make_txt():
    img_dir = "D:/1.work/mAP/input/images-optional/"
    extension = "*.jpg"
    txt_save = "D:/1.work/mAP/input/result.txt"

    files = sorted(glob.glob(img_dir + extension))
    
    for file in files:
        f = open(txt_save, 'a')
        f.write(file + "\n")
        print(file)


if __name__ == "__main__":
    make_txt()
  

