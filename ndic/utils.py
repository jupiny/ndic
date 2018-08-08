# -*- coding: utf-8 -*-

"""
This module provides utility functions that are used within Ndic

"""
from __future__ import absolute_import

import requests
from bs4 import BeautifulSoup

from ndic.constants import NAVER_ENDIC_URL
from ndic.exceptions import NdicConnectionError


def make_naver_endic_url(search_word):
    """
    Return NAVER dictionary url which contains the value of
    search word parameter

    """

    naver_endic_url = NAVER_ENDIC_URL.format(
        search_word=search_word,
    )
    return naver_endic_url


def request_naver_endic_url(naver_endic_url):
    """
    Send a GET request to NAVER dictionary url

    """

    try:
        response = requests.get(naver_endic_url)
    except requests.ConnectionError:
        raise NdicConnectionError()
    return response


def get_word_meaning(response, xth):
    """
    Parse a HTML document and get a text of xth meaning
    from particular tags
    By default, xth = 1
    """

    dom = BeautifulSoup(response.content, "lxml")
    div_element = dom.select_one(".word_num") or None
    word_meaning = ""
    if div_element:
        word_meaning_elements = div_element.select(".fnt_k05")
        meaning_cnt = len(word_meaning_elements)
        if 1 <= xth and xth <= meaning_cnt:
            word_meaning = word_meaning_elements[xth-1].text
    return word_meaning
