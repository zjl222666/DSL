from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup


setup(
    name='DSL_For_server',
    version='0.1',
    description='DSL',
    author='2019211168',
    license='Apache License, Version 2.0',
    keywords='DSL',
    packages=[
        'DSL',
        'DSL.core',
        'DSL.API',
        'DSL.server',
        'DSL.util',
    ],
    install_requires=[
        'easydict',
        'pytest>=5.0.0',
        
    ]
)
