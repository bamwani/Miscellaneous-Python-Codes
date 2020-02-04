# from flask import Flask
import os
import requests
import threading

path = '/home/kochar/Desktop/api/detected/'

def upload_n_move():
#    if condition:
#       t.stop()
    threading.Timer(15.0, upload_n_move).start() #every 15 seconds
    for r, d, f in os.walk(path):
        # try:
        for file in f:
            if '.jpg' in file:
                with open(str(path+file), 'rb') as f:
                    r = requests.post('URL TO SEND IMAGES', files={'image': f})
                os.rename(str(path+file), './done_d/'+str(file))
upload_n_move()
