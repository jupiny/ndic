# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def ndic(search_word):
    """
    Search the word in English-Korean and Korean-English dictionaries and return the corresponding Korean word(s) or English word(s). 

    Args:
        search_word: the word which user want to search 
    Returns:
        English word(s) or Korean word(s) corresponding to the search_word 
    Raises:
        ConnectionError: if network connection is lost.

    """
    naver_dict_url = "http://endic.naver.com/search.nhn?sLn=kr&searchOption=all&query="
    try:
        response = requests.get(naver_dict_url+search_word)
    except requests.ConnectionError:
        return "Network connection is lost. Please check the connection to the Internet."
    dom = BeautifulSoup(response.content, "html.parser")
    search_word_element = dom.select_one(".fnt_e30") or None
    word_meaning_element = dom.select_one(".fnt_k05") or None
    word_meaning = ""
    if search_word_element and search_word_element.select_one('strong'):
        word_meaning = word_meaning_element.text
    return word_meaning
