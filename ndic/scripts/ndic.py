from __future__ import unicode_literals

import requests
from bs4 import BeautifulSoup
import click


@click.command()
@click.argument('search_word')
def ndic(search_word):
    """
    Search the SEARCH_WORD in English-Korean and Korean-English dictionaries and return the corresponding Korean word(s) or English word(s). 

    """
    naver_dict_url = "http://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query="
    try:
        response = requests.get(naver_dict_url+search_word)
    except requests.ConnectionError:
        click.echo("Network connection is lost. Please check the connection to the Internet.")
        return
    dom = BeautifulSoup(response.content, "lxml")
    search_word_element = dom.select_one(".fnt_e30") or None
    word_meaning_element = dom.select_one(".fnt_k05") or None
    word_meaning = ""
    if search_word_element and search_word_element.select_one('strong'):
        word_meaning = word_meaning_element.text
    click.echo(word_meaning)
