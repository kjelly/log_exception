#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import log_exception

setup(

    name = 'log_exception',
    version = '0.0.1',
    description = 'log exception, including local vars.',
    long_description = open('README.md').read(),

    author = 'ya790206',
    url = 'https://github.com/ya790206/log_exception',
    license = 'Apache License Version 2.0',
    platforms = 'any',
    classifiers = [
    ],

    packages = find_packages(),

    entry_points = {
    }

)
