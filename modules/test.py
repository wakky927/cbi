import numpy as np

from b import template_matching


if __name__ == "__main__":
    rand = np.random.rand(100)
    a = np.array([1, 2, 3, 4, 5, 6], dtype=np.uint8)
    print(template_matching(a))
