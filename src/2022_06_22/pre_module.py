from decimal import Decimal, ROUND_HALF_UP

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
            dist = np.sqrt((x - width // 2) ** 2 + (y - height // 2) ** 2)
            n = norm.pdf(dist, loc=0, scale=sd)
            image[y, x] = int(np.clip(n * s * scale + low + rd[y, x], 0, 255))
    return image


def sab_pixel_analysis(ji, r):
    res = np.zeros((1, 2))

    for j, i in zip(ji[0], ji[1]):
        if 0 < j < r.shape[0] - 1 and 0 < i < r.shape[1] - 1:
            # judge whether peak value or not among 3x3
            if r[j, i] == np.amax(r[j-1:j+2, i-1:i+2]):
                eps_x = 0.5 * (np.log(r[j, i - 1]) - np.log(r[j, i + 1])) \
                        / (np.log(r[j, i - 1]) + np.log(r[j, i + 1]) - 2 * np.log(r[j, i]))
                eps_y = 0.5 * (np.log(r[j - 1, i]) - np.log(r[j + 1, i])) \
                        / (np.log(r[j - 1, i]) + np.log(r[j + 1, i]) - 2 * np.log(r[j, i]))

                # quantize
                eps_x = float(Decimal(str(eps_x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
                eps_y = float(Decimal(str(eps_y)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))

                res = np.vstack([res, [j + eps_y, i + eps_x]])

    return np.unique(res[1:, :], axis=0)  # Exclude duplicates just in case...


def detect_tracer(img, tracer_im, threshold):
    res = cv2.matchTemplate(img, tracer_im, cv2.TM_CCORR_NORMED)
    res_j, res_i = np.where(res > threshold)

    pp_yx = sab_pixel_analysis(ji=[res_j, res_i], r=res)

    return pp_yx
