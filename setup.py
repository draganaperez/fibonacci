#!/usr/local/bin/python3.4

import sys
from os.path import dirname
from setuptools import setup, find_packages

# make sure the current directory is in the python import path
sys.path.append(dirname(__file__))

# project dependencies
install_requires = [
    'configurate==0.4.0',
    'flake8',
    'flask==0.10',
    'Flask-RESTful==0.3.3',
    'setuptools',
]

# Setuptools configuration, used to create python .eggs and such.
# See: http://bashelton.com/2009/04/setuptools-tutorial/ for a nice
# setuptools tutorial.
setup(
    name="fibonacci_service",
    version="0.1",

    # packaging infos
    package_data={'': ['*.yaml', '*.html']},
    packages=find_packages(exclude=['test', 'test.*']),

    install_requires=install_requires,

    entry_points={
        'console_scripts': [
            #'fibonacci_api = app:run'
        ]
    },

    zip_safe=False
)
