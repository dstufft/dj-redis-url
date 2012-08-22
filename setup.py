#!/usr/bin/env python
"""
DJ-Database-URL
===============

This simple Django utility allows you to utilize the
`12factor <http://www.12factor.net/backing-services>`_ inspired
``REDIS_URL`` environment variable to configure your Django application.


Usage
-----

Configure your Redis database in ``settings.py`` from ``REDIS_URL``::

    REDIS = {"default": dj_redis_url.config()}

Parse an arbitrary Database URL::

    REDIS = {"default": dj_redis_url.parse("redis://..."")}

Installation
------------

Installation is simple too::

    $ pip install dj-redis-url
"""
from setuptools import setup

setup(
    name="dj-redis-url",
    version="0.1.3",

    description="Use Redis URLs in your Django Application.",
    long_description=__doc__,
    url="https://github.com/dstufft/dj-redis-url",

    author="Donald Stufft",
    author_email="donald.stufft@gmail.com",

    extras_require={
        "tests": ["pytest"],
    },

    py_modules=["dj_redis_url"],
    include_package_data=True,

    zip_safe=False,
)
