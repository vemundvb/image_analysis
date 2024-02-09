import cv2
import numpy as np

# Step 1: Read the grayscale image
image_path = 'gray.jpeg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Step 2: Convert the image to a 2D array
array_2d = np.array(gray_image)

# Step 3: Loop through the array and set each value to 0
for i in range(array_2d.shape[0]):
    for j in range(array_2d.shape[1]):
        array_2d[i, j] = 100

# Step 4: Create a new image from the modified 2D array
new_image_path = 'new_image.jpg'
cv2.imwrite(new_image_path, array_2d)

# Display the original and modified images (optional)
cv2.imshow('Original Image', gray_image)
cv2.imshow('Modified Image', array_2d.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
