import os
import sys

import cv2
import numpy as np
from tqdm import tqdm


user = os.environ["USER"]
SUPER_DIR = f"/media/{user}/ボリューム/M2"
Q_DIR = [
    "cbi_q_1",
    "cbi_q_2",
    "cbi_q_3"
]
# SUB_DIR = [
#     "C001H001S0001",
#     "C001H001S0002",
#     "C001H001S0003",
#     "C001H001S0004",
#     "C001H001S0005",
#     "C001H001S0006",
#     "C001H001S0007",
#     "C001H001S0008",
#     "C001H001S0009",
#     "C001H001S0010",
# ]

TRACER_IMGS_LIGHT_DIR = "tracer_imgs_light"

THRESHOLD = 0.96


def crop_img_light(im):
    return im[290:910, 90:820, :]


def is_same(ij, r):
    for a in range(-5, 6):
        for b in range(-5, 6):
            if (ij[0]+a, ij[1]+b) in r:
                return True
    return False


def mark_tracer_light(im):
    res_list = []

    for t in range(600):
        tracer_im = cv2.imread(TRACER_IMGS_LIGHT_DIR + f"/tracer_{t}.bmp")
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

    sub_dir = args[1]

    for q_dir in Q_DIR:
        for f in tqdm(range(1, 10001)):
            FILE = SUPER_DIR + "/original/2022_04_10/" + q_dir + "/" + sub_dir + "/" + sub_dir + f"{f:06}.bmp"
            img = cv2.imread(FILE)
            img = crop_img_light(im=img)
            result = mark_tracer_light(im=img)
            np.savetxt(
                SUPER_DIR + "/result/2022_04_10/pre/" + q_dir + "/" + sub_dir + f"/{f:06}.csv",
                result,
                delimiter=',', fmt="%d", header="(i, j) of upper left coordinates."
            )

    print(0)
