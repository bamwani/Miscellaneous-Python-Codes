#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:13:53 2020

@author: Bamwani
"""
#Play RTSP link in opencv
import cv2

cam = cv2.VideoCapture("rtsp link")

while True:
    _,frame = cam.read()
    cv2.imshow("feed",frame)
    if cv2.waitKey(1) == 27:
        break
