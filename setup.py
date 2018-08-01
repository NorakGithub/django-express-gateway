#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'django>=2',
    'djangorestframework>=3.7',
    'requests>=2.19'
]

setup_requirements = [
    'pytest-runner',
    'setuptools-git-version'
]

test_requirements = [
    'pytest',
    'django-test-without-migrations',
    'responses',
]

setup(
    name='django_express_gateway',
    version='{tag}',
    author="Khemanorak Khath",
    author_email='khath.khemanorak@gmail.com',
    keywords='django, express, gateway, express_gateway',
    description="Integrating Django with Express Gateway",
    license="MIT license",
    include_package_data=True,
    long_description=readme + '\n\n' + history,
    url='https://github.com/NorakGithub/django_express_gateway',
    packages=find_packages(include=['django_express_gateway']),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=requirements,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
