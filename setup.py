#!/usr/bin/env python

import os

from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='eng2ipa',
    version='0.0.1',
    package_dir={'': '.'},
    zip_safe=True,
    include_package_data=False,
    description='Converts English text to IPA notation',
)
