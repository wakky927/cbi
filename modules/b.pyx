import cython
import numpy as np
cimport numpy as np


DTYPE = np.int
DTYPE2 = np.float
ctypedef np.int_t DTYPE_t
ctypedef np.float_t DTYPE_t2


def template_matching(np.ndarray[DTYPE_t, ndim=2] f, np.ndarray[DTYPE_t, ndim=2] g, np.ndarray[DTYPE_t, ndim=2] m):
    # get array size
    cdef int f_M = f.shape[0]
    cdef int f_N = f.shape[1]
    cdef int g_M = g.shape[0]
    cdef int g_N = g.shape[1]

    # set result array
    cdef int g_m = g_M // 2 - 1
    cdef int g_n = g_N // 2 - 1
    #
    # cdef int h_M = f_M + 2 * g_m + 1
    # cdef int h_N = f_N + 2 * g_n + 1
    cdef np.ndarray[DTYPE_t2, ndim=2] h = np.zeros([f_M, f_N], dtype=DTYPE2)

    # set val
    cdef int x, y, s, t, ss, tt
    cdef int s_from, s_to, t_from, t_to

    cdef DTYPE_t value1
    cdef DTYPE_t2 value2, value3

    for x in xrange(f_M):
        for y in xrange(f_N):
            if m[x, y] == 0:
                h[x, y] = 0.0
            else:
                s_from = max(g_m - x, -g_m)
                s_to = min((f_M - x) - g_m, g_m + 1)
                t_from = max(g_n - y, -g_n)
                t_to = min((f_N - y) - g_n, g_n + 1)
                value1 = 0
                value2 = 0
                value3 = 0

                for s in xrange(s_from, s_to):
                    for t in xrange(t_from, t_to):
                        ss = x - g_m + s
                        tt = y - g_n + t

                        value1 += g[g_m - s, g_n - t] * f[ss, tt]
                        value2 += f[ss, tt] * f[ss, tt]
                        value3 += g[g_m - s, g_n - t] * g[g_m - s, g_n - t]

                h[x, y] = value1 / np.sqrt(value2 * value3)

    return h
