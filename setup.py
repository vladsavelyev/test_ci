#!/usr/bin/env python
import sys
py_v = sys.version_info[:2]
if py_v < (3, 6):
    sys.exit('Only Python 3.6 and higher are supported. Current version: ' + '.'.join(py_v))

from os.path import join
import os

name = 'test_travis'
script_name = 'test_travis'
package_name = 'test_travis'


version = os.environ.get('TRAVIS_TAG', 'dev')

from setuptools import setup, find_packages
setup(
    name=name,
    version=version,
    author='Vlad Saveliev and Alla Mikheenko',
    author_email='vladislav.sav@gmail.com',
    description='Genome capture target coverage evaluation tool',
    long_description=(open('README.md').read()),
    keywords='bioinformatics',
    url='https://github.com/vladsaveliev/bed_annotation',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
