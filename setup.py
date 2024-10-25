# -*- coding: utf-8 -*-
# setup.py for redisbayes, updated for Python 3.11 compatibility

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="redisbayes",
    version="1.0.0",  # Alternatively, import version from the module if defined there
    description=u"Naïve Bayesian Text Classifier on Redis",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",  # If README.md is Markdown
    author="Justine Tunney",
    author_email="jtunney@gmail.com",
    url="https://github.com/jart/redisbayes",
    license="MIT",
    install_requires=[
        "redis>=4.0.0"  # Update redis to a compatible version for Python 3.11
    ],
    py_modules=["redisbayes"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Database",
        "Topic :: Communications :: Email",
    ],
)
