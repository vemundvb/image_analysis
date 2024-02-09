import cv2
import numpy as np







array = [1,4,6,4,1]

matrix = np.outer(array, array)

matrix_sum = np.sum(matrix)

normalized_matrix = matrix / matrix_sum

print(normalized_matrix)







