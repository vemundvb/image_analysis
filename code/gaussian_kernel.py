from scipy.ndimage import gaussian_filter
import numpy as np
import cv2


image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
result = np.zeros_like(gray_image)

# gaussian filter

array = [1,4,6,4,1]
w = 2
matrix = np.outer(array, array)

matrix_sum = np.sum(matrix)


normalized_matrix = matrix / matrix_sum
print(normalized_matrix)


height, width = gray_image.shape

for i in range(1, height - 1):
    for j in range(1, width - 1):
        block = gray_image[i-1:i+1,j-1:j+1]
        
        
