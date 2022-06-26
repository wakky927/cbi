import cv2
import numpy as np
from scipy.stats import norm


def gauss_circle(image, sd, high=255, low=0, random_sd=0):
    height, width = image.shape[:2]
    rd = np.random.normal(0, random_sd, (height, width))
    scale = high - low
    s = 1 / norm.pdf(0, loc=0, scale=sd)

    for y in range(0, height):
        for x in range(0, width):
            dist = np.sqrt((x - width//2) ** 2 + (y - height//2) ** 2)
            n = norm.pdf(dist, loc=0, scale=sd)
            image[y, x] = int(np.clip(n * s * scale + low + rd[y, x], 0, 255))
    return image


def detect_tracer(img, sample_img):
    pass


if __name__ == '__main__':
    im = cv2.imread("gauss_circle_size_9_sd_2.bmp")
    sample = cv2.imread("gauss_circle_size_9_sd_2.bmp")
    