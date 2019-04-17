'''
Created: 2019-04-16 22:36:34
Author : Wensheng Cheng
-----
Copyright (c) 2019 Wensheng Cheng.
'''

# This code visualizes labels with class format. 
import cv2
from pathlib import Path
import natsort

#labels_in_class_format:(0,1,2,3,4)
IMG_Path = Path("class_labels_folder")
IMG_File = natsort.natsorted(list(IMG_Path.glob("*.bmp")), alg=natsort.PATH)
IMG_Str = []
for i in IMG_File:
    IMG_Str.append(str(i))

#make sure the out_prefix ends with '/'(linux) or '\'(windows)
out_prefix="output_images_folder/"
for k in range(len(IMG_Str)):
    pic = cv2.imread(IMG_Str[k],1)
    pic[pic == 1] = 100
    pic[pic == 2] = 150
    pic[pic == 3] = 200
    pic[pic == 4] = 250
    out_path=out_prefix+Path(IMG_Str[k]).name
    cv2.imwrite(out_path,pic)

