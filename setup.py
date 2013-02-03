#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
      name = 'pyaoa',
      version = '0.1',
      description = 'Python Android Open Accessory library',
      author = 'Laco Pápay',
      author_email = 'laco.papay@gmail.com',
      license = 'BSD',
      url='http://github.com/lacop/pyaoa',
      packages=['aoa'],
      install_requires=['pyusb']
)
