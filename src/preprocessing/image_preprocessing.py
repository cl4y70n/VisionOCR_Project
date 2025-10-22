
import cv2
import numpy as np

def preprocess_image(image):
    img = np.array(image.convert('L'))  # grayscale
    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return img_bin
