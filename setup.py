#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'launchpadlib']

test_requirements = ['pytest>=3', ]

setup(
    author="Phil Roche",
    author_email='phil.roche@canonical.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="CLI tool to view the MPs that you have reviewed for a given launchpad project.",
    entry_points={
        'console_scripts': [
            'launchpad_mp_review_inspector=launchpad_mp_review_inspector.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='launchpad_mp_review_inspector',
    name='launchpad_mp_review_inspector',
    packages=find_packages(include=['launchpad_mp_review_inspector', 'launchpad_mp_review_inspector.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/philroche/launchpad_mp_review_inspector',
    version='0.0.1',
    zip_safe=False,
)
