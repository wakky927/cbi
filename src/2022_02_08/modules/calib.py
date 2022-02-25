import numpy as np


def px2mm(data):
    length = 22
    x0, y0 = 507, 181
    x1, y1 = 567, 181
    alpha = length / np.sqrt((x0 - x1)**2 + (y0 - y1)**2)

    return data * alpha


def f2s(data):
    fps = 300

    return data * fps
