# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pkg_resources import get_distribution

from ndic.search import search


__version__ = get_distribution('ndic').version

__all__ = [
    'search',
]
