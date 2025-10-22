
import os
from PIL import Image

def load_images_from_folder(folder_path):
    images = []
    filenames = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(folder_path, filename))
            images.append(img)
            filenames.append(filename)
    return images, filenames
