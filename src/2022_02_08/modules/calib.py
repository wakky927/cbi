import numpy as np


def px2mm(data):
    length = 0
    x0, y0 = 0, 0
    x1, y1 = 0, 0
    alpha = length / np.sqrt((x0 - x1)**2 + (y0 - y1)**2)

    return data * alpha


def f2s(data):
    fps = 300

    return data * fps
