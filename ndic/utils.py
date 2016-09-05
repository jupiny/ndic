# -*- coding: utf-8 -*-
from __future__ import absolute_import

import requests
from bs4 import BeautifulSoup

from ndic.constants import NAVER_ENDIC_URL
from ndic.exceptions import NdicConnectionError


def make_naver_endic_url(search_word):
    naver_endic_url = NAVER_ENDIC_URL.format(
        search_word=search_word,
    )
    return naver_endic_url


def request_naver_endic_url(naver_endic_url):
    try:
        response = requests.get(naver_endic_url)
    except requests.ConnectionError:
        raise NdicConnectionError()
    return response


def get_word_meaning(response):
    dom = BeautifulSoup(response.content, "lxml")
    search_word_element = dom.select_one(".fnt_e30") or None
    word_meaning = ""
    if search_word_element and search_word_element.select_one('strong'):
        word_meaning_element = dom.select_one(".fnt_k05")
        word_meaning = word_meaning_element.text
    return word_meaning
