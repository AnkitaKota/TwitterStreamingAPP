#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['tweepy','configparser','pymongo',]

test_requirements = ['pytest>=3', ]

setup(
    author="Ankita Kota",
    author_email='ankikota@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Twitter streaming data and persisting it in DB",
    entry_points={
        'console_scripts': [
            'twitter_streaming_app=twitter_streaming_app.cli:main',
        ],
    },
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='twitter_streaming_app',
    name='twitter_streaming_app',
    packages=find_packages(include=['twitter_streaming_app', 'twitter_streaming_app.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AnkitaKota/twitter_streaming_app',
    version='0.1.0',
    zip_safe=False,
)
