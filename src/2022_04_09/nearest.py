from collections import deque

import numpy as np
from tqdm import tqdm


SUPER = "G:\\M2\\result\\2022_04_09\\"


class Vector2D(object):
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


class TP(object):
    def __init__(self, idx):
        self.idx = idx
        self.p0 = 0
        self.p1 = 0
        self.err = 0.0
        self.flag = False


def nearest(imgs):
    pp0, pp1 = imgs[0], imgs[1]

    if pp0 is None or pp1 is None:
        return None

    result = np.zeros([pp0.shape[0], 4])

    dx = Vector2D
    pp01 = [TP(idx=x) for x in range(pp0.shape[0])]
    s = 20  # search window
    npa = -1  # the number of available particle
    ntsp = 0  # the number for tracking the same particle

    for ii in range(pp0.shape[0]):  # 1st
        flag = True  # init flag for the particle tracking
        c, cc = 1e10, 1e10  # arbitrary large number

        for jj in range(pp1.shape[0]):  # 2nd
            dx.x = pp1[jj][0] - pp0[ii][0]
            dx.y = pp1[jj][1] - pp0[ii][1]

            cc = np.sqrt(dx.x ** 2 + dx.y ** 2)

            if cc <= s and cc < c:
                c = cc

                if flag:
                    npa += 1

                pp01[npa].p0 = ii
                pp01[npa].p1 = jj
                pp01[npa].err = c
                pp01[npa].flag = True
                flag = False

    # post-processing
    # If different particles track the same particle,
    # giving an error flag to particle which has larger error.
    for ii in range(npa):
        if pp01[ii].flag:
            for jj in range(ii + 1, npa):
                if pp01[ii].p1 == pp01[jj].p1:
                    if pp01[ii].err > pp01[jj].err:
                        pp01[ii].flag = False
                        ntsp += 1
                        break
                    else:
                        pp01[jj].flag = False
                        ntsp += 1

    for ii in range(npa+1):
        if pp01[ii].flag:
            result[ii][0] = pp0[pp01[ii].p0][0]
            result[ii][1] = pp0[pp01[ii].p0][1]
            result[ii][2] = pp1[pp01[ii].p1][0] - pp0[pp01[ii].p0][0]
            result[ii][3] = pp1[pp01[ii].p1][1] - pp0[pp01[ii].p0][1]

    return result[:npa]


if __name__ == '__main__':
    for q in [1, 2, 3, 15, 25]:
        for t in tqdm(range(1, 11)):
            IN_DIR = SUPER + f"pre\\cbi_q_{q}\\C001H001S{t:04}\\"
            OUT_DIR = SUPER + f"ptv\\nearest_skip_5\\cbi_q_{q}\\{t}\\"

            d0, d1, d2, d3, d4 = deque([None, None]), deque([None, None]), deque([None, None]), deque([None, None]), \
                deque([None, None])
            DATA = [d0, d1, d2, d3, d4]

            for i in range(1, 5001, 5):
                for j in range(5):
                    DATA[j].popleft()

                    tmp = np.loadtxt(IN_DIR + f"{i + j:06}.csv", delimiter=',', skiprows=1)
                    if tmp.ndim == 1:
                        if len(tmp) > 0:
                            tmp = tmp[np.newaxis, :]
                        else:
                            tmp = None
                    elif tmp.ndim == 2:
                        pass
                    else:
                        tmp = None

                    DATA[j].append(tmp)

                    r = nearest(imgs=DATA[j])

                    if r is not None and r != []:
                        np.savetxt(OUT_DIR + f"{i + j:06}.csv", r, fmt='%.18f', delimiter=',', header="x, y, dx, dy")

        print(f"cbi_q_{q} fin. ")
    print("fin. ")
