#!/usr/bin/env python3
# coding: utf-8

from setuptools import find_packages
from setuptools import setup

setup(
    name='$name$',
    version='$version$',
    description='$desc$',
    url='$url$',
    author='$author$',
    author_email='$author_email$',
    install_requires=[
        'typing-extensions>=3.6.2,<=4.0.0',
    ],
    license='$license$',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: $python_version$',
    ],
    keywords=[
    ],
    packages=find_packages(exclude=[
        'tests',
    ]),
    entry_points={
        'console_scripts': [],
    },
)
