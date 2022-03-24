import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)

classes = ['','']

while True:
    sucess, img = cap.read()

    cv2.imshow('Image',img)
    cv2.waitKey(1)