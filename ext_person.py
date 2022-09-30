import os
from shutil import copyfile
from pathlib import Path
from tqdm import tqdm

# current txt/image path
txt_path = "D:/2.dataset/coco/original/YOLO/"
jpg_path = "D:/2.dataset/COCO/original/train2017/"

# new txt/image path
out_txt_path = "D:/2.dataset/COCO/person_txt/"
out_jpg_path ="D:/2.dataset/COCO/person_jpg/"

Path(out_txt_path).mkdir(parents=True, exist_ok=True)
Path(out_jpg_path).mkdir(parents=True, exist_ok=True)

txt_list = os.listdir(txt_path)
txt_list = map(lambda x: x.split("/")[-1], txt_list)
txt_list = map(lambda x: x.split(".")[0], txt_list)

for filename in tqdm(txt_list):
    filepath = os.path.join(txt_path, filename) + ".txt"
    with open(filepath, "r") as infile:
        data = infile.readlines()

    for x in data:
        if x.startswith("0"):
            out_file_path = os.path.join(out_txt_path, filename) + ".txt"
            with open(out_file_path, "a") as outfile:
                outfile.write(x)

            if not os.path.exists(os.path.join(out_jpg_path, x) + ".jpg"):
                jpg_file = os.path.join(jpg_path, filename) + ".jpg"
                out_jpg_file = os.path.join(out_jpg_path, filename) + ".jpg"
                copyfile(jpg_file, out_jpg_file)