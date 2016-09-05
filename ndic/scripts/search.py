# -*- coding: utf-8 -*-
from __future__ import absolute_import

import click

from ndic.search import search


@click.command()
@click.argument('search_word')
def cli_search(search_word):
    """
    Search the SEARCH_WORD in English-Korean and Korean-English dictionaries
    and return the corresponding Korean word(s) or English word(s).

    """
    word_meaning = search(search_word)
    click.echo(word_meaning)
