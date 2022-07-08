import sys

import cv2
import numpy as np
from tqdm import tqdm

import pre_module


def pre_at_x_100_mm(args):
    in_dir = args[2]
    out_dir = args[3]

    width, height = 15, 15
    image = np.zeros((height, width), dtype=np.uint8)
    sample_img = pre_module.gauss_circle(image.copy(), 2)

    for n in tqdm(range(1, 22542)):
        img = cv2.imread(in_dir + in_dir[-14:-1] + f"{n:06}.bmp", 0)
        img = img[115:, 140:900]

        pp_yx = pre_module.detect_tracer(img=img, tracer_im=sample_img, threshold=0.6)
        np.savetxt(out_dir + f"pp_{n}.csv", pp_yx, fmt='%.1f', delimiter=',', header="pp_y, pp_x")


def main(args):
    if args[1] == '100':
        pre_at_x_100_mm(args)
    elif args[1] == 200:
        pass
    else:
        print("ERROR!")


if __name__ == '__main__':
    main(sys.argv)
