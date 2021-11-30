from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup


setup(
    name='gobigger',
    version='0.1',
    description='DSL',
    author='2019211168',
    license='Apache License, Version 2.0',
    keywords='Go-Bigger DI',
    packages=[
        'gobigger',
        'gobigger.agents',
        'gobigger.balls',
        'gobigger.server',
        'gobigger.utils',
        'gobigger.managers',
        'gobigger.players',
        'gobigger.render',
        'gobigger.leagues'
    ],
    install_requires=[
        'easydict',
        'gym>=0.15.3',  # pypy incompatible
        'pygame>=2.0.0',
        'pytest>=5.0.0',
        # 'sphinx_toolbox',
        'opencv-python',
        'numpy>=1.10',
        'matplotlib',
        'trueskill'
    ]
)
