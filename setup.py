#!/usr/bin/env python

from distutils.core import setup

setup(
    name='upcwifioff',
    version='0.1.2',
    author='Maximilian Fellner',
    author_email='max.fellner@gmail.com',
    url='https://github.com/mfellner/upcwifioff',
    license='MIT',
    packages=['upcwifioff'],
    install_requires=[
        'selenium>=3.0.2,<4',
        'splinter>=0.7.5,<1',
        'tqdm>=4.10.0,<5'
    ],
    entry_points={
      'console_scripts': [
          'upcwifioff = upcwifioff.__main__:main'
      ]
    }
)
