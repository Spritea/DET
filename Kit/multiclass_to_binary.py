'''
Created: 2019-04-16 22:24:05
Author : Wensheng Cheng
-----
Copyright (c) 2019 Wensheng Cheng.
'''

# This code changes multiclass labels to binary labels.
import cv2
from pathlib import Path
import natsort

#multiclass_labels_folder
IMG_Path = Path("multiclass_labels_folder")
IMG_File = natsort.natsorted(list(IMG_Path.glob("*.bmp")), alg=natsort.PATH)
IMG_Str = []
for i in IMG_File:
    IMG_Str.append(str(i))

#make sure the out_prefix ends with '/'(linux) or '\'(windows)
out_prefix="output_images_folder/"
for k in range(len(IMG_Str)):
    pic = cv2.imread(IMG_Str[k],1)
    pic[pic > 0] = 1
    out_path=out_prefix+Path(IMG_Str[k]).name
    cv2.imwrite(out_path,pic)


