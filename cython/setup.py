from distutils.core import setup
from Cython.Build import cythonize

setup(name='check and search modules',
      ext_modules=cythonize("check.pyx"))
