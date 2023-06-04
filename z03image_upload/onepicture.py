import cv2
from tensorflow import image
import numpy as np


def path_to_img_flu(path_flu):
    img_flu = cv2.imread(path_flu)
    img_flu = image.per_image_standardization(img_flu[42:122, 42:122, :])
    img_flu = np.array(img_flu).astype('float32') / 255
    img_flu = np.expand_dims(img_flu, axis=0)  # (80, 80, 3)-->(1, 80, 80, 3)
    return img_flu

def path_to_img_mix(path_mix):
    img_mix = cv2.imread(path_mix)
    img_mix = image.per_image_standardization(img_mix[42:122, 42:122, :])
    img_mix = np.array(img_mix).astype('float32') / 255
    img_mix = img_mix[:, :, 0:1]  # input2 是一层
    img_mix = np.expand_dims(img_mix, axis=0)

    return img_mix