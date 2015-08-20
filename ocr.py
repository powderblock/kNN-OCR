from math import *
import sys
import re
import numpy as np
import cv2
import sys
from collections import *

def distance(a, b):
    return sqrt(sum((a - b) ** 2 for a, b in zip(a, b)))

def classify(a, dataset):
    distances = []
    for item in dataset:
        distances.append(((distance(a, item[0])), item[1]))
    return sorted(distances)[0][1]

images = []

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

for letter in letters:
    for i in range(5):
        print letter+"{0}.png".format(i)
        img = cv2.imread("letters/"+letter+"{0}.png".format(i))

        width = img.shape[0]
        height = img.shape[1]

        pixels = []

        # For every pixel in the image:
        for x in range(height):
            for y in range(width):
                red = img[y, x, 2]
                green = img[y, x, 1]
                blue = img[y, x, 0]
                if red == 255 and green == 255 and blue == 255:
                    pixels.append(1)
                else:
                    pixels.append(0)

        images.append((pixels, letter))

def arrayOutput(img):
    img = cv2.imread(img)

    width = img.shape[0]
    height = img.shape[1]

    pixels = []

    # For every pixel in the image:
    for x in range(height):
        for y in range(width):
            red = img[y, x, 2]
            green = img[y, x, 1]
            blue = img[y, x, 0]
            if red == 255 and green == 255 and blue == 255:
                pixels.append(1)
            else:
                pixels.append(0)
    return pixels

print classify(arrayOutput("classify/classf.png"), images)
