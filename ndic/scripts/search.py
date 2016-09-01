# -*- coding: utf-8 -*-
from __future__ import absolute_import

import requests
from bs4 import BeautifulSoup
import click

from ndic.constants import NAVER_ENDIC_URL
from ndic.exceptions import NdicConnectionError


@click.command()
@click.argument('search_word')
def search(search_word):
    """
    Search the SEARCH_WORD in English-Korean and Korean-English dictionaries
    and return the corresponding Korean word(s) or English word(s).

    """
    naver_endic_url = NAVER_ENDIC_URL.format(
        search_word=search_word,
    )
    try:
        response = requests.get(naver_endic_url)
    except requests.ConnectionError:
        raise NdicConnectionError
    dom = BeautifulSoup(response.content, "lxml")
    search_word_element = dom.select_one(".fnt_e30") or None
    word_meaning_element = dom.select_one(".fnt_k05") or None
    word_meaning = ""
    if search_word_element and search_word_element.select_one('strong'):
        word_meaning = word_meaning_element.text
    click.echo(word_meaning)
