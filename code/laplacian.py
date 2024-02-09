import cv2
import numpy as np

# Load the image
image_path = 'smoothing.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the Laplacian kernel
laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

# Initialize an array to store the Laplacian result
laplacian_result = np.zeros_like(gray_image)

# Get image dimensions
height, width = gray_image.shape

# Apply Laplacian filter
for i in range(1, height - 1):
    for j in range(1, width - 1):
        # Compute the convolution
        convolution = np.sum(gray_image[i - 1:i + 2, j - 1:j + 2] * laplacian_kernel)
        laplacian_result[i, j] = np.clip(convolution, 0, 255)  # Clip to ensure values are within valid range

# Convert to uint8
laplacian_result = np.uint8(laplacian_result)

# Save the resulting image
cv2.imwrite('laplacian_result.jpg', laplacian_result)

print("Done")
