#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
with open(path.join(here, 'dota2/__init__.py'), encoding='utf-8') as f:
    __version__ = f.readline().split('"')[1]

install_requires = [
    'steam[client]>=0.8.0',
    'gevent-eventemitter>=1.4',
    'gevent>=1.1',
    'protobuf>=3.0.0b2',
]

if sys.version_info < (3, 4):
    install_requires.append('enum34>=1.0.4')

setup(
    name='dota2',
    version=__version__,
    description='Module for interacting Dota2\'s Game Coordinator',
    long_description=long_description,
    url='https://github.com/ValvePython/dota2',
    author="Rossen Georgiev",
    author_email='rossen@rgp.io',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='valve steam steamid api webapi',
    packages=['dota2'] + ['dota2.'+x for x in find_packages(where='dota2')],
    install_requires=install_requires,
    zip_safe=True,
)
