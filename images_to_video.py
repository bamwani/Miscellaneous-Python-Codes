#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:13:53 2020

@author: Bamwani
"""
# Create a video of images.
import cv2
import numpy as np
import glob
import imutils
 
img_array = []
for filename in glob.glob('path/to/images/folder'):
    # print(filename)
    img = cv2.imread(filename)
    # img = imutils.resize(img, width=720)

    height, width, layers = img.shape
    size = width,height
    img_array.append(img)
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*"XVID"), 13, size)
print(len(img_array))
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
