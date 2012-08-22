# -*- coding: utf-8 -*-

import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


# Register database schemes in URLs.
urlparse.uses_netloc.append("redis")

DEFAULT_ENV = "REDIS_URL"


def config(env=DEFAULT_ENV, default=None, **overrides):
    """Returns configured REDIS dictionary from REDIS_URL."""

    config = {}

    s = os.environ.get(env, default)

    if s:
        config = parse(s)

    overrides = dict([(k.upper(), v) for k, v in overrides.items()])

    config.update(overrides)

    return config


def parse(url):
    """Parses a database URL."""

    config = {}

    url = urlparse.urlparse(url)

    # Remove query strings.
    path = url.path[1:]
    path = path.split('?', 2)[0]

    # Update with environment configuration.
    config.update({
        "DB": int(path or 0),
        "PASSWORD": url.password,
        "HOST": url.hostname,
        "PORT": url.port,
    })

    return config
