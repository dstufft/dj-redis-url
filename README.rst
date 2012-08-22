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
