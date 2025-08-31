# Write a Python program to visualize RGB channels.

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img_path = r"C:\Users\shiva\OneDrive\Pictures\MU.jpg"
img = Image.open(img_path)
img_array = np.array(img)

# Split channels (0=Red, 1=Green, 2=Blue)
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

# Create RGB visualizations
zeros = np.zeros_like(R)

red_channel = np.stack([R, zeros, zeros], axis=2)
green_channel = np.stack([zeros, G, zeros], axis=2)
blue_channel = np.stack([zeros, zeros, B], axis=2)

# Plot
plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
plt.imshow(img_array)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(red_channel)
plt.title("Red Channel")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(green_channel)
plt.title("Green Channel")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(blue_channel)
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()
