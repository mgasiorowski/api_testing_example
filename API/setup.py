#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requirements():
    with open("requirements.txt") as requirements_file:
        return [line.strip() for line in requirements_file]


def main():
    __version__ = '0.0.1'
    __package_name__ = 'test_api'
    __description__ = 'API for automate testing with different tool and languages'
    __url__ = 'https://github.com/mgasiorowski/api_testing_example/API/test_api'
    __author__ = "mgasiorowski"
    __requirements__ = get_requirements()

    setup(
        name=__package_name__,
        long_description=__description__,
        version=__version__,
        url=__url__,
        author=__author__,
        platforms=['unix', 'linux', 'osx'],
        classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: POSIX',
            'Topic :: Software Development :: Libraries',
            'Topic :: System :: Distributed Computing',
            'Topic :: System :: Networking',
            'Programming Language :: Python'],
        install_requires=__requirements__,
        zip_safe=False,
        include_package_data=True
    )


if __name__ == '__main__':
    main()
