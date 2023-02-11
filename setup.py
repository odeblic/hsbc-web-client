#!/usr/bin/env python

from setuptools import setup, find_packages
from hsbc_web_client import __author__, __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hsbc-web-client',
    version=__version__,
    author=__author__,
    description='Client for HSBC web interface (Hong Kong and France only) to fetch list of accounts with their balance.',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=find_packages('hsbc_web_client'),
    install_requires=['selenium', 'webdriver-manager'],
    license='WTFPL',
    zip_safe=True,
)
