#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name='blockfinder',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_require=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        blockfinder=blockfinder:cli
    ''',
    test_suite='block_finder.test',
)
