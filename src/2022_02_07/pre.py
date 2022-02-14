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

    src_pts = np.array([[125, 174], [125, 812], [795, 833], [806, 170]], dtype=np.float32)
    dst_pts = np.array([[250, 173], [250, 789], [797, 809], [806, 170]], dtype=np.float32)
    mat = cv2.getPerspectiveTransform(src_pts, dst_pts)

    src_pts2 = np.array([[0, 0], [0, 633], [602, 633], [602, 0]], dtype=np.float32)
    dst_pts2 = np.array([[30, 0], [30, 633], [602, 633], [602, 0]], dtype=np.float32)
    mat2 = cv2.getPerspectiveTransform(src_pts2, dst_pts2)

    for i in range(start, end):
        f = in_dir + f"_{i:08}.bmp"
        img = cv2.imread(f, 0)
        p_img = cv2.warpPerspective(img, mat, (1280, 1024))
        t_img = image.trim(p_img, [175, 250], [808, 852])
        p_img2 = cv2.warpPerspective(t_img, mat2, (602, 633))
        t_img2 = image.trim(p_img2, [0, 30], [633, 602])
        cv2.imwrite(out_dir + f"_{i:08}.bmp", t_img2)


def main(args):
    if args[1] == "b":
        bg(args)
    elif args[1] == "s":
        sub_bg(args)
    elif args[1] == "c":
        calib(args)
    else:
        print("ERROR!")


if __name__ == '__main__':
    main(sys.argv)
