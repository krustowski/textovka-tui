#!/usr/bin/env python3

from setuptools import setup

setup(
    name='textovka-tui',
    version='1.0',
    packages=['source'],
    url='https://github.com/krustowski/textovka-tui',
    license='MIT',
    author='krustowski',
    author_email='k@n0p.cz',
    description='REST API text-based game in TUI',
    install_requires=[
        'requests==2.31.0',
        'npyscreen==4.10.5'
    ]
)
