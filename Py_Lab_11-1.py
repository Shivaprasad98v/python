# Write a Python program to display details of an image (dimension of an image, shape of an image, min pixel value at channel B).

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img_path = r"C:\Users\shiva\OneDrive\Pictures\MU.jpg"
img = Image.open(img_path)

# Convert to numpy array
img_array = np.array(img)

# Dimensions (width x height)
dimensions = img.size   # (width, height)

# Shape of image array
shape = img_array.shape  # (height, width, channels)

# Minimum pixel value at Blue channel (channel index 2 if RGB)
min_blue = img_array[:, :, 2].min()

# Display details
print("Image Dimensions (Width x Height):", dimensions)
print("Image Shape (Height, Width, Channels):", shape)
print("Minimum Pixel Value in Blue Channel:", min_blue)

# Optional: Display the image
plt.imshow(img_array)
plt.title("Input Image")
plt.axis("off")
plt.show()
