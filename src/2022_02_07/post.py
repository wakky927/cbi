import sys

from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm


def ave(args):
    dx, dy = None, None
    dx_c, dy_c = None, None

    in_dir = args[3]
    out_dir = args[4]

    if args[2] == "cbi":
        flag = True

        for i in tqdm(range(3200)):
            if flag:
                flag = False
                dx = np.loadtxt(in_dir + f"dx_{i}_{i + 1}.csv", delimiter=',')
                dy = np.loadtxt(in_dir + f"dy_{i}_{i + 1}.csv", delimiter=',')
                dx_c = np.where(dx == np.nan, 0, 1)
                dy_c = np.where(dy == np.nan, 0, 1)
            else:
                dx = np.nansum([dx, np.loadtxt(d + f"dx_{i}_{i + 1}.csv", delimiter=',')], axis=0)
                dy = np.nansum([dy, np.loadtxt(d + f"dy_{i}_{i + 1}.csv", delimiter=',')], axis=0)
                dx_c += np.where(np.loadtxt(d + f"dx_{i}_{i + 1}.csv", delimiter=',') == np.nan, 0, 1)
                dy_c += np.where(np.loadtxt(d + f"dy_{i}_{i + 1}.csv", delimiter=',') == np.nan, 0, 1)

        dx /= dx_c
        dy /= dy_c

    np.savetxt(dx, out_dir + "ave_dx.csv", delimiter=',')
    np.savetxt(dy, out_dir + "ave_dy.csv", delimiter=',')

    return dx, dy


def graph(args):
    in_dir = args[3]
    out_dir = args[4]

    dx = np.loadtxt(in_dir + "ave_dx.csv", delimiter=',')
    dy = np.loadtxt(in_dir + "ave_dy.csv", delimiter=',')

    n = 48
    width, height = 739, 692

    x, y = np.meshgrid(np.linspace(width, 0, n, dtype="int"), np.linspace(0, height, n, dtype="int"))

    fig, ax = plt.subplots(figsize=(24, 20))
    c = np.sqrt(dx ** 2 + dy ** 2)
    im = ax.quiver(x, y, -dx, dy, c, cmap="jet")
    fig.colorbar(im)
    im.set_clim(0, 4)

    plt.savefig(out_dir + "ave.png")


def main(args):
    if args[1] == "ave":
        _ = ave(args)
    elif args[1] == "graph":
        graph(args)
    else:
        print("ERROR!")


if __name__ == '__main__':
    main(sys.argv)
