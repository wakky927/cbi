def bg(bg_dir_path, z_range, mode=0):
    """
    create background image
    :param bg_dir_path: path of bg dir
    :param z_range: img z-range(start, stop, iter)
    :param mode: minimum(= 0) or mean(= 1)
    :return: bg img
    """
    im = None

    if mode == 0 or mode == "min":
        for i in range(*z_range):
            path = bg_dir_path + f"_{i:08}.bmp"

            if im is None:
                im = cv2.imread(path, 0)
            else:
                im = np.minimum(im, cv2.imread(path, 0))

        return im

    elif mode == 1 or mode == "mean" or mode == "avg":
        t = 0
        for i in range(*z_range):
            path = bg_dir_path + f"_{i:08}.bmp"
            t += 1

            if im is None:
                im = cv2.imread(path, 0)
            else:
                im += cv2.imread(path, 0)

        return im / t

    else:
        return None


def trim(im, ul, br):
    """
    trimming image
    :param im: img
    :param ul: upper left coordinate(j, i)
    :param br: bottom right coordinate(j, i)
    :return: trimmed img
    """
    return im[ul[0]:br[0], ul[1]:br[1]]
