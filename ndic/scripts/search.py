# -*- coding: utf-8 -*-

"""
This module provides functions for searching the word
in command line interface by Ndic

"""
from __future__ import absolute_import

import click

from ndic.search import search


@click.command()
@click.argument('search_word')
@click.option('--xth', '-x', default=1, help='xth meaning. default=1')
def cli_search(search_word, xth):
    """
    Search the SEARCH_WORD in English-Korean and Korean-English dictionaries
    and echo the corresponding Korean word(s) or English word(s).

    """
    word_meaning = search(search_word, xth)
    click.echo(word_meaning)


if __name__ == '__main__':
    cli_search()
