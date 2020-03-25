#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
import sys
from setuptools import setup

if sys.hexversion < 0x02070000:
    raise RuntimeError("Python 2.7 or higher required")

# Replace all instances of `comp-neurosci-skeleton` with the name of your project
setup(
    name="crcns-pfc5-ak2cw-jk9ah",
    version="0.0.1",
    package_dir={'crcns-pfc5-ak2cw-jk9ah': 'src'},
    packages=["crcns-pfc5-ak2cw-jk9ah"],

    description="",
    long_description="",
    install_requires=[
        "numpy>=1.10",
    ],

    author="Amrutha Kadali, Jeewoo Kim",
    maintainer='Amrutha Kadali, Jeewoo Kim',
)
