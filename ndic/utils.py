# -*- coding: utf-8 -*-

"""
This module provides utility functions that are used within Ndic

"""
from __future__ import absolute_import

import requests
from bs4 import BeautifulSoup

from ndic.constants import NAVER_ENDIC_URL, NAVER_ZHDIC_URL
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


def make_naver_zhdic_url(search_word):
    """
    Return naver chinese-zh dictionary url which contains the value of
    search word parameter

    :parameter search_word: chinese word
    :type search_word: String

    """

    encoded_chinese = requests.utils.quote(search_word)
    naver_zhdic_url = NAVER_ZHDIC_URL.format(
        search_word=encoded_chinese,
    )
    return naver_zhdic_url


def request_naver_endic_url(naver_endic_url):
    """
    Send a GET request to NAVER dictionary url

    """

    try:
        response = requests.get(naver_endic_url)
    except requests.ConnectionError:
        raise NdicConnectionError()
    return response


def request_naver_zhdic_url(naver_zhdic_url):
    """
    Send a GET request to NAVER zh-dictionary url

    """

    try:
        response = requests.get(naver_zhdic_url)
    except requests.ConnectionError:
        raise NdicConnectionError()
    return response.json()


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


def stringify_zh_result(zh_json):
    """
    stringify zh_json
    :param zh_json:
    e.g.)
    [
        {
            'entryNameTTS': '你',
            'meanList': [
                {'meaning': '너. 자네. 당신.', 'poomsa': '대명사'},
                {'meaning': '너희들. 당신들.', 'poomsa': '대명사'},
                {'meaning': '사람. 누구. (어떤 사람을 막연히 일컫거나 때로는 자기를 의미하기도 함)', 'poomsa': '대명사'}
            ],
            'pinyin': 'nǐ'},
        {
            'entryNameTTS': '你的',
            'meanList': [
                {'meaning': '너의.', 'poomsa': ''},
                {'meaning': '네 것.', 'poomsa': '명사'},
                {'meaning': '이새끼.', 'poomsa': '명사'}],
            'pinyin': 'nǐ‧de'
        },
        {
            'entryNameTTS': '你看你',
            'meanList': [
                {'meaning': '네 꼴 좀 봐라!', 'poomsa': ''}
            ],
            'pinyin': 'nǐkànnǐ'},
        {
            'entryNameTTS': '你瞧你',
            'meanList': [
                {'meaning': '네 꼴 좀 봐라.', 'poomsa': ''}
            ],
            'pinyin': 'nǐqiáonǐ'
        },
        {
            'entryNameTTS': '迷你',
            'meanList': [
                {'meaning': '미니(mini). 소형의.', 'poomsa': '형용사'}
            ],
            'pinyin': 'mínǐ'
        }
    ]
    :type zh_json: list
    :return:
    returns string
    e.g.)

    """

    ret = ""

    for item in zh_json:
        single_line = "\n"

        single_line += "{entryNameTTS}({pinyin})\n".format(
            entryNameTTS=item["entryNameTTS"],
            pinyin=item["pinyin"],
        )

        for mean in item["meanList"]:
            poomsa = mean["poomsa"]
            meaning = mean["meaning"]
            relatedMeanInfos = mean["relatedMeanInfos"]

            if poomsa != "":
                single_line += "[{poomsa}] ".format(poomsa=poomsa)

            if meaning != "":
                single_line += "{meaning} ".format(meaning=meaning)

            if relatedMeanInfos: # if empty
                for related in relatedMeanInfos:
                    single_line += "\n[{relatedTypeString}] {destEntryName}({destEntryPinyin}) ".format(
                        relatedTypeString=related["relatedTypeString"],
                        destEntryName=related["destEntryName"],
                        destEntryPinyin=related["destEntryPinyin"],
                    )

            single_line += "\n"

        ret += single_line

    return ret
