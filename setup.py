#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='sphinxcontrib-rdf',
    version='0.1.0',
    description='Sphinx contrib extension for working with RDF and RDFLib',
    long_description=readme + '\n\n' + history,
    author='Wes Turner',
    author_email='wes@wrd.nu',
    url='https://github.com/westurner/sphinxcontrib-rdf',
    packages=find_packages(),
    package_dir={'sphinxcontrib.rdf': 'sphinxcontrib/rdf'},
    include_package_data=True,
    install_requires=[
        'Sphinx>=0.6',
        'RDFLib',
    ],
    license="BSD",
    zip_safe=False,
    keywords='rdf sphinxcontrib sphinx rdflib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    namespace_packages=['sphinxcontrib'],
    test_suite='tests',
)
