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


# def sab_pixel_interpolation(ij, r):
#     for a in range(-5, 6):
#         for b in range(-5, 6):
#             if (ij[0]+a, ij[1]+b) in r:
#                 return True
#     return False


def detect_tracer(img, tracer_im, threshold):

    res = cv2.matchTemplate(img, tracer_im, cv2.TM_CCORR_NORMED)
    res_j, res_i = np.where(res > threshold)

    return res_j, res_i

