import cv2
import numpy as np

def sharpen(image):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    new_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow('Sharpened Image', new_image)
    cv2.waitKey(0)
    return new_image

def blur(image):
    kernels = [3,4,5,7,9,15]
    for idx, k in enumerate(kernels):
        image_bl = cv2.blur(image, ksize = (k,k))
        cv2.imshow(str(k), image_bl)
        cv2.waitKey(0)
    return

def resize(fname, width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    org_height, org_width = image.shape[0:2]
    print('width:', org_width)
    print('height: ', org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    return fname, new_image



filename, new_image = resize('bird.jpg', 1280, 960)
cv2.imshow('resized image', new_image)
cv2.waitKey(0)

#blur(new_image)
image = sharpen(new_image)