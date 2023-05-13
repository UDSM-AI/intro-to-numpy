import numpy as np
from PIL import Image

# Load image
image = Image.open('img.JPG')

# Convert image to NumPy array
image_array = np.array(image)

# Rotate image by 90 degrees
# rotated_array = np.rot90(image_array)
# print(rotated_array)
# Convert NumPy array back to image and save
# rotated_image = Image.fromarray(rotated_array)
# rotated_image.save('rotated_image_.jpg')
print(image_array.shape)
