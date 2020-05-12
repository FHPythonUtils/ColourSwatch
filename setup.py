# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='colourswatch',
    version='2020',
    description='Use this module to read, and write to a number of colour palette file formats',
    python_requires='==3.*,>=3.5.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/ColourSwatch/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/ColourSwatch",
        "repository":
            "https://github.com/FHPythonUtils/ColourSwatch"
    },
    author='FredHappyface',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=['ColourSwatch'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'colormath==3.*,>=3.0.0', 'defusedxml==0.*,>=0.6.0',
        'gimpformats==2020.*,>=2020.2.2', 'pyyaml==5.*,>=5.3.1'
    ],
)
