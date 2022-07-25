import sys

import cv2
import numpy as np

from modules import image


def bg(args):
    in_dir = args[2]
    out_dir = args[3]
    start = int(args[4])
    end = int(args[5])
    mode = args[6]

    z_range = [start, end, 1]
    b_img = image.bg(bg_dir_path=in_dir, z_range=z_range, mode=mode)
    cv2.imwrite(out_dir + f"bg.bmp", b_img)


def sub_bg(args):
    in_dir = args[2]
    out_dir = args[3]
    start = int(args[4])
    end = int(args[5])
    bg_img_path = args[6]

    b_img = cv2.imread(bg_img_path, 0)

    for i in range(start, end):
        f = in_dir + f"_{i:08}.bmp"
        img = cv2.imread(f, 0)
        s_img = cv2.subtract(img, b_img)
        cv2.imwrite(out_dir + f"_{i:08}.bmp", s_img)


def calib(args):
    in_dir = args[2]
    out_dir = args[3]
    start = int(args[4])
    end = int(args[5])

    src_pts = np.array([[291, 301], [303, 902], [1024, 855], [1027, 306]], dtype=np.float32)
    dst_pts = np.array([[290, 376], [299, 881], [827, 842], [830, 381]], dtype=np.float32)
    mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

    for i in range(start, end):
        f = in_dir + f"_{i:08}.bmp"
        img = cv2.imread(f, 0)
        p_img = cv2.warpPerspective(img, mat, (1280, 1024))
        t_img = image.trim(p_img, [372, 258], [883, 828])
        cv2.imwrite(out_dir + f"_{i:08}.bmp", t_img)


def main(args):
    if args[1] == "b":
        bg(args)
    elif args[1] == "gx_32_gy_32_t_32_s_64_th_70":
        sub_bg(args)
    elif args[1] == "c":
        calib(args)
    else:
        print("ERROR!")


if __name__ == '__main__':
    main(sys.argv)
