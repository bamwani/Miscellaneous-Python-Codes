#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:13:53 2020

@author: Bamwani
"""

import threading
import cv2

#this function will keep on running forever
def printit():
#    if condition:
#        t.stop()
    t = threading.Timer(5.0, printit)
    t.start()
    print ("Hello, World!")

printit()



cam = cv2.VideoCapture("rtsp link")

while True:
    _,frame = cam.read()
    cv2.imshow("a",frame)
    cv2.waitKey(1)
