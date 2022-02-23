from matplotlib import pyplot as plt
import numpy as np


if __name__ == '__main__':
    width, height = 739, 692
    n = 48

    for i in range(300):
        x, y = np.meshgrid(np.linspace(0, width, n, dtype="int"), np.linspace(0, height, n, dtype="int"))

        ave_dx = np.loadtxt(f"../../data/1/dx_{i}_{i+1}.csv", delimiter=',')
        ave_dy = np.loadtxt(f"../../data/1/dy_{i}_{i+1}.csv", delimiter=',')
        fig, ax = plt.subplots(figsize=(22, 20))
        c = np.sqrt(ave_dx ** 2 + ave_dy ** 2)

        # velocity normalize
        ave_dx /= c
        ave_dy /= c

        x = x[1::2, 1::2]
        y = y[1::2, 1::2]
        ave_dx = ave_dx[1::2, 1::2]
        ave_dy = ave_dy[1::2, 1::2]
        c = c[1::2, 1::2]

        im = ax.quiver(x, y, -ave_dx, ave_dy, c, cmap="jet", scale_units='xy', scale=0.035, width=0.015)
        ax.invert_xaxis()
        fig.colorbar(im)
        im.set_clim(0, 1.5)
        # plt.show()
        plt.savefig(f"../../data/_1/{i}_{i+1}.png", dpi=300)

    print(0)
