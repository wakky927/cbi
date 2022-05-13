import os


import cv2
import numpy as np


def adjust(img, alpha=1.0, beta=0.0):
    res = alpha * img + beta
    return np.clip(res, 0, 255).astype(np.uint8)


if __name__ == '__main__':
    file = os.listdir("original/")

    for f in file:
        src = cv2.imread("original/" + f)
        dst = adjust(src, alpha=3.0, beta=30.0)
        cv2.imwrite("adj/" + f, dst)
