#!/usr/bin/env python
from os.path import join
from setuptools import setup, find_packages
from versionpy import get_version, find_package_files, get_reqs

pkg = 'test_ci'
version = get_version(pkg)

setup(
    name=pkg,
    script_name=pkg,
    version=version,
    author='Vlad Saveliev',
    author_email='vladislav.sav@gmail.com',
    description='Genome capture target coverage evaluation tool',
    long_description=(open('README.md').read()),
    long_description_content_type="text/markdown",
    url='https://github.com/vladsaveliev/test_ci',
    license='GPLv3',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    keywords='bioinformatics',
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
