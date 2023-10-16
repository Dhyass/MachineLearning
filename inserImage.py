# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:08:53 2023

@author: NONZOOU
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread(r'C:\Users\NONZOOU\Pictures\jol.PNG')

# Check if the image was loaded successfully
if image is not None:
    # Convert the image to a NumPy array
    image_np = np.array(image)

    # Display the image using Matplotlib
    plt.imshow(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
    plt.axis('on')  # Hide the axis labels and ticks
    plt.show()
    print(image_np.shape)
    
else:
    print("Failed to load the image.")


# Load the image using OpenCV
image2 = cv2.imread(r'C:\Users\NONZOOU\Pictures\jol.PNG')

# Check if the image was loaded successfully
if image2 is not None:
    # Convert the image to a NumPy array
    image_np2 = np.array(image2)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image_np2, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    plt.imshow(grayscale_image, cmap='gray')
    plt.axis('off')  # Hide the axis labels and ticks
    plt.show()
    print(grayscale_image.shape)
    
    h = grayscale_image.shape[0]
    w = grayscale_image.shape[1]
    
    zoomm_jol= grayscale_image[0:-h//2, w//4:-w//4]
    
    plt.imshow(zoomm_jol, cmap='gray')
    plt.show()
else:
    print("Failed to load the image.")