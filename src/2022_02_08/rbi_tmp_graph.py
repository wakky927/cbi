from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm

from modules import calib


IN_DIR = "/media/takuya/exHDD/M1/result/2022_02_08/post/gx_32_gy_32_t_32_s_64_th_70/"
OUT_DIR = "/media/takuya/exHDD/M1/result/2022_02_08/graph/gx_32_gy_32_t_32_s_64_th_70/"


def graph(dx, dy, out_path):
    width, height = 739, 693
    n = 32

    x, y = np.meshgrid(np.linspace(693, -46, n, dtype="int"), np.linspace(0, height, n, dtype="int"))
    x = calib.px2mm(x)
    y = calib.px2mm(y)

    fig, ax = plt.subplots(figsize=(36, 30))
    plt.xlabel("$r$ [mm]", fontsize=100)
    plt.ylabel("$h$ [mm]", fontsize=100)
    plt.xticks(fontsize=100)
    plt.yticks(fontsize=100)
    c = np.sqrt(dx ** 2 + dy ** 2)

    dx /= c
    dy /= c

    x = x[:, :-2]
    y = y[:, :-2]
    dx = dx[:, :-2]
    dy = dy[:, :-2]
    c = c[:, :-2]

    im = ax.quiver(x, y, -dx, dy, c, cmap="jet", scale_units='xy', scale=0.12, width=0.0045)

    pp = fig.colorbar(im)
    for tt in pp.ax.get_yticklabels():
        tt.set_fontsize(100)
    pp.set_label('$\sqrt{u^2+v^2}$ [mm/s]', fontsize=100)
    im.set_clim(0, 120)
    plt.savefig(out_path, dpi=300)

    plt.cla()
    plt.clf()
    plt.close()


if __name__ == '__main__':
    for t in tqdm(range(500, 1501, 500)):
        for q in range(1, 4):
            for i in range(0, 300):
                ave_dx = calib.f2s(calib.px2mm(np.loadtxt(IN_DIR + f"500_{t}/{q}/dx_{i}_{i+1}.csv", delimiter=',')))
                ave_dy = calib.f2s(calib.px2mm(np.loadtxt(IN_DIR + f"500_{t}/{q}/dy_{i}_{i+1}.csv", delimiter=',')))

                graph(dx=ave_dx, dy=ave_dy, out_path=OUT_DIR+f"500_{t}/{q}/dx_dy_{i}_{i+1}.png")
