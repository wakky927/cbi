from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy


ext = Extension("b", sources=["b.pyx"], include_dirs=[numpy.get_include()])
setup(name="b", ext_modules=cythonize([ext]))
