# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 23:04:36 2021

@author: gm
"""

import cv2


cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow("WebCam", frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()