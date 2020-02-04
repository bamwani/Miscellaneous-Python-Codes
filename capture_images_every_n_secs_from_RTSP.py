#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:13:53 2020

@author: Bamwani
"""

import threading
import cv2
import datetime
# print (str(datetime.time.now()))
cam = cv2.VideoCapture("rtsp link")

def saveit():
    threading.Timer(20.0, saveit).start()
    try:
        name = "./images/" + str(datetime.datetime.now()) + ".jpg"
        print(name)
        cv2.imwrite(name, frame)
    except:
        pass
saveit()
while True:
    _,frame = cam.read()
    # cv2.imshow("a",frame)
    # # saveit()
    # cv2.waitKey(1)
    
