from typing import Tuple
from facenet_pytorch import MTCNN
from PIL import Image
from tqdm import tqdm
import os
import glob
import torch
import pathlib


def main():
    base_path = "D:/2.dataset/COCO/"
    image_path = os.path.join(base_path, "person_jpg")
    label_path = os.path.join(base_path, "person_txt")
    images = glob.glob(os.path.join(image_path, "*.jpg"))
    files = list(map(lambda x: pathlib.Path(x).stem, images))

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Running on device : {}".format(device))

    mtcnn = MTCNN(device=device)

    for file in tqdm(files):
        img = os.path.join(image_path, file + ".jpg")
        image = Image.open(img).convert('RGB')
        width, height = image.size

        boxes, _ = mtcnn.detect(image) # [x_top_left, y_top_left, x_bottom_right, y_bottom_right]

        if boxes is not None:
            for box in boxes:
                box = map(lambda x: 0 if x < 0 else x, box)
                x, y, w, h = convert_mtcnn_to_datknet(*box, width, height)
                with open(os.path.join(label_path, file + ".txt"), "a") as f:
                    f.write(f"1 {x} {y} {w} {h}\n")

def convert_mtcnn_to_datknet(x1: int, y1: int, x2: int, y2: int, width: int, height: int) -> Tuple[float]:
    darknet_x = (x1+ x2) / 2 / width
    darknet_y = (y1 + y2) / 2 / height
    darknet_width = (x2 -x1)/ width
    darknet_height = (y2 - y1) / height
    
    return darknet_x, darknet_y, darknet_width, darknet_height

if __name__=="__main__":
    main()