#!/usr/bin/env python
import os
from setuptools import setup

pkg = 'test_ci'

try:
    import versionpy
except ImportError:
    res = input('Installation requires versionpy. Install it now? [Y/n]')
    if res.lower().startswith('n'):
        raise
    os.system('pip install versionpy')
    import versionpy

version = versionpy.get_version(pkg)
package_data = {
    pkg: versionpy.find_package_files('', pkg)
}

setup(
    name=pkg,
    script_name=pkg,
    version=version,
    author='Vlad Savelyev',
    author_email='vladislav.sav@gmail.com',
    description='Toy repo to test CI',
    long_description=(open('README.md').read()),
    long_description_content_type="text/markdown",
    url=f'https://github.com/vladsaveliev/{pkg}',
    license='GPLv3',
    packages=[pkg],
    package_data=package_data,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'versionpy',
        'click',
        'ngs_utils'
    ],
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
