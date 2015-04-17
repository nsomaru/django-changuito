#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-changuito',
    version='0.7.1',
    description='A fork of django-cart with the same simplicity but up-to-date',
    maintainer='Angel Velasquez',
    maintainer_email='nsomaru@gmail.com',
    license="LGPL v3",
    url='https://github.com/nsomaru/django-changuito',
    packages=['changuito'],
    install_requires=[
        'django-fsm==2.2.0',
        'django-extensions==1.4.9',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],

    test_suite="runtests.runtests",
)
