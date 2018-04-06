#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


from bmga import __version__


setup(
    name='boxme-api',
    version=__version__,
    description='A flexible & capable API layer for Django.',
    author='DiepDT',
    author_email='diepdt@peacesoft.net',
    url='https://github.com/vituocgia/boxme-api',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'bmga',
        'bmga.utils',
        'bmga.management',
        'bmga.management.commands',
        'bmga.migrations',
        'bmga.contrib',
        'bmga.contrib.gis',
        'bmga.contrib.contenttypes',
    ],
    package_data={
        'bmga': ['templates/boxme/*'],
    },
    zip_safe=False,
    requires=[
        'python_mimeparse(>=0.1.4, !=1.5)',
        'dateutil(>=1.5, !=2.0)',
    ],
    install_requires=[
        'python-mimeparse >= 0.1.4, != 1.5',
        'python-dateutil >= 1.5, != 2.0',
    ],
    tests_require=['mock', 'PyYAML', 'lxml', 'defusedxml'],
    classifiers=[
        'Development Status :: Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
