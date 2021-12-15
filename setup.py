from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup

from SerWise.server import process
from SerWise.server.server import server


setup(
    name='SerWise',
    version='0.1',
    description='DSL for service',
    author='2019211168',
    license='Apache License, Version 2.0',
    keywords='DSL',
    packages=[
        'SerWise',
        'SerWise.core',
        'SerWise.API',
        'SerWise.server',
        'SerWise.util',
    ],
    install_requires=[
        'easydict',
        'pytest>=5.0.0',
        'rich==10.15.2',
        'pynput==1.7.5',
               
    ],
    entry_points = {
        'console_scripts': [
            'dslProcess = SerWise.server.process:main',
            'serwise = SerWise.server.server:main'
        ]
    },

)
