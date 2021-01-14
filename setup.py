#!/usr/bin/env python
import os
from setuptools import setup

pkg = 'test_ci'

setup(
    name=pkg,
    script_name=pkg,
    version='2.0.13',
    author='Vlad Savelyev',
    author_email='vladislav.sav@gmail.com',
    description='Toy repo to test CI',
    long_description=(open('README.md').read()),
    long_description_content_type="text/markdown",
    url=f'https://github.com/vladsaveliev/{pkg}',
    license='GPLv3',
    packages=[pkg],
    include_package_data=True,
    zip_safe=False,
    scripts=['scripts/vcf2mt'],
    keywords='bioinformatics',
    classifiers=[
        'Environment :: Console',
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
