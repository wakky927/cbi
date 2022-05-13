import os
import sys

import cv2
import numpy as np
from tqdm import tqdm

import adj


Q_DIR = [
    "cbi_q_1",
    "cbi_q_2",
    "cbi_q_3",
    "cbi_q_15",
    "cbi_q_25"
]

TRACER_IMGS_DARK_DIR = "tracer_imgs_dark"

THRESHOLD = 0.97


def crop_img_top(im):
    return im[0:310, :, :]


def crop_img_left(im):
    return im[290:800, :110, :]


def crop_img_right(im):
    return im[290:800, 800:, :]


def is_same(ij, r):
    for a in range(-5, 6):
        for b in range(-5, 6):
            if (ij[0]+a, ij[1]+b) in r:
                return True
    return False


def mark_tracer_dark(im):
    res_list = []

    for t in range(600):
        tracer_im = cv2.imread(TRACER_IMGS_DARK_DIR + f"/tracer_{t}.bmp")
        res = cv2.matchTemplate(im, tracer_im, cv2.TM_CCORR_NORMED)
        res_j, res_i = np.where(res > THRESHOLD)

        for n in range(len(res_i)):
            i, j = res_i[n], res_j[n]
            if is_same((i, j), res_list):
                continue
            res_list.append((i, j))

    return res_list


if __name__ == '__main__':
    args = sys.argv

    SUPER = args[1]
    sub_dir = args[2]

    for q_dir in Q_DIR:
        for f in tqdm(range(1, 5001)):
            FILE = SUPER + "/original/2022_04_09/" + q_dir + "/" + sub_dir + "/" + sub_dir + f"{f:06}.bmp"

            img = cv2.imread(FILE)

            img = adj.adjust(img, alpha=3.0, beta=30.0)

            img_top = crop_img_top(im=img)
            img_left = crop_img_left(im=img)
            img_right = crop_img_right(im=img)

            result_top = mark_tracer_dark(im=img_top)
            result_left = mark_tracer_dark(im=img_left)
            result_right = mark_tracer_dark(im=img_right)

            np.savetxt(
                SUPER + "/result/2022_04_09/pre_dark/top/" + q_dir + "/" + sub_dir + f"/{f:06}.csv",
                result_top,
                delimiter=',', fmt="%d", header="(i, j) of upper left coordinates."
            )
            np.savetxt(
                SUPER + "/result/2022_04_09/pre_dark/left/" + q_dir + "/" + sub_dir + f"/{f:06}.csv",
                result_left,
                delimiter=',', fmt="%d", header="(i, j) of upper left coordinates."
            )
            np.savetxt(
                SUPER + "/result/2022_04_09/pre_dark/right/" + q_dir + "/" + sub_dir + f"/{f:06}.csv",
                result_right,
                delimiter=',', fmt="%d", header="(i, j) of upper left coordinates."
            )

    print(0)
