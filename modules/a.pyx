# distutils: language=c++
# distutils: extra_compile_args = ["-O3"]
# cython: language_level=3, boundscheck=False, wraparound=False
# cython: cdivision=True

ctypedef long long LL

cpdef LL sum_typed_memoryviews(LL[:] s):
    cdef LL ret = 0
    cdef LL l = s.shape[0]
    cdef LL i
    for i in range(l):
        ret += s[i]
    return ret
