# -*- coding: utf-8 -*-

"""
This module provides functions for searching the word
in command line interface by Ndic

"""
from __future__ import absolute_import

import click

from ndic.search import search, search_zh_cli


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


@click.command()
@click.argument('search_word')
@click.option('--number', '-n', default=1, help='number of result, default=1')
def cli_search_zh(search_word, number):
    """
    Search the SEARCH_WORD in Chinese-Korean dictionaries
    and echo the corresponding Results

    Example Usage)

        >>> ndic-zh 你好 --number=1

        >>> ndic-zh 你好 -n1

    :param search_word: chinese word
    :param number: number of results

    """
    search_result = search_zh_cli(search_word, number)
    click.echo(search_result)
