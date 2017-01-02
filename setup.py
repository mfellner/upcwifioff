#!/usr/bin/env python

from distutils.core import setup

setup(
    name='upcwifioff',
    version='0.1.1',
    author='Maximilian Fellner',
    author_email='max.fellner@gmail.com',
    url='https://github.com/mfellner/upcwifioff',
    license='MIT',
    packages=['upcwifioff'],
    entry_points={
      'console_scripts': [
          'my_project = upcwifioff.__main__:main'
      ]
    }
)
