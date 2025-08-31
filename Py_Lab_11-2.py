# Write a Python program to padding black spaces.

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img_path = r"C:\Users\shiva\OneDrive\Pictures\MU.jpg"
img = Image.open(img_path)
img_array = np.array(img)

# Padding size (top, bottom, left, right)
top, bottom, left, right = 50, 50, 100, 100

# Create black canvas
height, width, channels = img_array.shape
new_height = height + top + bottom
new_width = width + left + right

# Black background (zeros)
padded_img = np.zeros((new_height, new_width, channels), dtype=np.uint8)

# Place original image in the center
padded_img[top:top+height, left:left+width, :] = img_array

# Display result
plt.imshow(padded_img)
plt.title("Padded Image with Black Borders")
plt.axis("off")
plt.show()
