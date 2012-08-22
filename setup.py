#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="dj-redis-url",
    version="0.1",

    description="Use Redis URLs in your Django Application.",
    long_description=open("README.rst").read(),
    url="https://github.com/dstufft/dj-redis-url",
    license=open("LICENSE").read(),

    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",

    extras_require={
        "tests": ["pytest"],
    },

    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
)
