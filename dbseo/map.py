import glob
import os
from pathlib import Path
from PIL import Image

txt_path = "D:/2.dataset/coco/map/txt/"
img_path = "D:/1_develop/face_detection/coco_dataset/person/image/"

out_path = "D:/1.work/mAP/input/ground-truth/"
Path(out_path).mkdir(parents=True, exist_ok=True)

txt_list = os.listdir(txt_path)
txt_list = map(lambda x: x.split("/")[-1], txt_list)
txt_list = map(lambda x: x.split(".")[0], txt_list)

def convert(detection, img_width, img_height):
    j = detection.split()
    class_name = j[0]
    x = float(j[1])
    y = float(j[2])
    w = float(j[3])
    h = float(j[4])

    #left, top, right, bottom
    left = int((x - w * 0.5) * img_width)
    top = int((y - h * 0.5) * img_height)
    right = int((x + w * 0.5) * img_width)
    bottom = int((y + h * 0.5) * img_height)

    return f"{class_name} {left} {top} {right} {bottom}\n"


def main():
    for filename in txt_list:
        filepath = os.path.join(txt_path, filename) + ".txt"
        outpath = os.path.join(out_path, filename) + ".txt"

        with open(filepath, 'r') as f:
            lines = f.readlines()

        data = list(map(lambda x: x.rstrip(), lines))

        img = Image.open(img_path + filename + ".jpg") 
        img_w, img_h = img.size

        result = ''.join([convert(x, img_w, img_h) for x in data])

        with open(outpath, 'w') as f:
            f.write(result)
      
        
    

if __name__ == "__main__":
    main()