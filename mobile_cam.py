# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 07:48:46 2019

@author: Rabin maharjan
"""
import urllib.request
import cv2
import numpy as np


# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.68:8080/shot.jpg'

while True:

    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break