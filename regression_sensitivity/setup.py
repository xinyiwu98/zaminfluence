# https://python-packaging.readthedocs.io/en/latest/minimal.html

from setuptools import setup

setup(name='regsens_rgiordandev',
      version='0.1',
      description='Regression sensitivity for AMIP',
      url='NA',
      author='Ryan Giordano',
      author_email='rgiordan@gmail.com',
      license='MIT',
      install_requires=[
        'numpy',
        'autograd >= 1.3',
        'paragami >= 0.42',
        'vittles >= 0.171',
        'ipykernel' ],
      packages=['regsens_rgiordandev'])

