import cv2
import numpy as np


image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
array_2d = np.array(gray_image)

image_path = 'smoothing.jpg'
smooth_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
smooth_2d = np.array(gray_image)



sharpened = np.zeros_like(array_2d)


for i in range(0, array_2d.shape[0] - 1):
    for j in range(0, array_2d.shape[1] - 1):
        sharpened[i,j] = array_2d[i,j] + 2 * smooth_2d[i,j]

new_image_path = 'sharp.jpg'
cv2.imwrite(new_image_path, sharpened)