# -*- coding: utf-8 -*-

"""
This module provides functions for searching the word by Ndic

"""
from __future__ import absolute_import

from ndic.utils import make_naver_endic_url, make_naver_zhdic_url
from ndic.utils import request_naver_endic_url, request_naver_zhdic_url
from ndic.utils import get_word_meaning, stringify_zh_result
from ndic.parser import parse_zh_json


def search(search_word, xth=1):
    """
    Search the word in English-Korean and Korean-English dictionaries
    and return the corresponding Korean word(s) or English word(s).

    Args:
        search_word: the word which user want to search
    Returns:
        English word(s) or Korean word(s) corresponding to the search_word
    Raises:
        NdicConnectionError: if network connection is lost.

    """
    naver_endic_url = make_naver_endic_url(search_word)
    response = request_naver_endic_url(naver_endic_url)
    word_meaning = get_word_meaning(response, xth)
    return word_meaning


def search_zh(search_word, xth=1):
    """
    Search chinese-zh

    Example Usage)

        >>> import ndic
        >>> ndic.search_zh("你")

    :param search_word:
    :param xth:
    :return:
    """
    naver_zhdic_url = make_naver_zhdic_url(search_word)
    response_json = request_naver_zhdic_url(naver_zhdic_url)
    items = parse_zh_json(response_json)

    return stringify_zh_result(items)

