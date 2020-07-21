import numpy as np
import matplotlib.pyplot as plt
import cv2
def resize(fname, width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)


resize('bird.jpg', 1280, 960)
