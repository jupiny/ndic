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
        xth: result index
    Returns:
        English word(s) or Korean word(s) corresponding to the search_word
    Raises:
        NdicConnectionError: if network connection is lost.

    """
    naver_endic_url = make_naver_endic_url(search_word)
    response = request_naver_endic_url(naver_endic_url)
    word_meaning = get_word_meaning(response, xth)
    return word_meaning


def search_zh_cli(search_word, num=1):
    """
    Search chinese-zh and return result converted to string
    for cli environment

    :param search_word: chinese or korean word
    :param num: number of result
    :return:
    """

    if num < 1:
        raise ValueError("search_zh_cli() got parameter res_len under 1")

    naver_zhdic_url = make_naver_zhdic_url(search_word)
    response_json = request_naver_zhdic_url(naver_zhdic_url)
    parsed_items = parse_zh_json(response_json, num)
    ret_string = stringify_zh_result(parsed_items)

    return ret_string


def search_zh(search_word, num=1):
    """
    Search chinese-zh and return result converted to string
    for python interpreter environment
    Example Usage)

        >>> import ndic
        >>> ndic.search_zh("你")

        >>> ndic.search_zh("시계", 3)

    :param search_word: chinese or korean word
    :param num: number of result
    :return:
    """

    if num < 1:
        raise ValueError("search_zh() got parameter res_len under 1")

    naver_zhdic_url = make_naver_zhdic_url(search_word)
    response_json = request_naver_zhdic_url(naver_zhdic_url)
    parsed_items = parse_zh_json(response_json, num)

    return parsed_items
