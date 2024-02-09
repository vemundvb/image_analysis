import cv2
import numpy as np

# Leser grayscale
image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Konverterer til 2d array
array_2d = np.array(gray_image)

# Lager kopy av array, som skal representere en smooth array
smoothed_array = np.zeros_like(array_2d)

# Algoritme for masken
def get_output_from_mask(center_i, center_j, cross_size):
    sum = 0
    half_way = int((cross_size - 1) / 2)
    
    for i in range(-half_way, half_way):
        for j in range(-half_way, half_way):
           try:
               sum += array_2d[center_i + i][center_j + j] 
           except IndexError:
               sum += 0
    
    return sum / (cross_size * cross_size)

dimension_size = 3

dim = (dimension_size - 1) / 2
# Looper hver pixel og legger på masken
for i in range(0, array_2d.shape[0] - 1):
    for j in range(0, array_2d.shape[1] - 1):
        smoothed_array[i, j] = np.sum( array_2d[i+dim:i-dim, j+dim:j-dim] ) / dimension_size



print("Done masking")

# Lager et nytt bilde fra den smoothe arrayen
new_image_path = 'smoothing.jpg'
cv2.imwrite(new_image_path, smoothed_array)
print("Done")



# ================== Sharpening image ================






