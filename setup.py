#!/usr/bin/env python

from setuptools import setup

setup(name='HSBC Web Client',
      version='1.0',
      description='Client for HSBC web interface (Hong Kong and France only) to fetch list of accounts with their balance.',
      # packages=['.']
      py_modules=['hsbc-web-client'],
      install_requires=['selenium', 'webdriver-manager'],
      license='WTFPL',
     )

