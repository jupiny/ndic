# -*- coding: utf-8 -*-
from .exceptions import CannotFindResultError

from bs4 import BeautifulSoup

def parse_zh_json(zh_json, num):
    """
    tidy up zh_json data and return tiny data
    :param zh_json:
    :param num: number of result
    :return:
    list
    e.g.)
    [
        {
            'origin': '你们',
            'meanings': ['너희들. 당신들. 자네들.'],
            'pinyin': 'nǐ‧men'
        },
        {
            'origin': '你们好',
            ...
        }
    ]
    """

    if type(zh_json) not in (dict, ):
        raise ValueError(
            "parse_zh_json() got wrong parameter zh_json"
            "expected dict type but got {} type".format(type(zh_json))
        )

    if "searchResults" not in zh_json:
        raise CannotFindResultError()

    if "searchEntryList" not in zh_json["searchResults"]:
        raise CannotFindResultError()

    items = zh_json["searchResults"]["searchEntryList"]["items"]

    ret = []
    for item in items:
        card = {
            "origin" : item["entryNameTTS"],
            "meanings": [ remove_html_tags(mean["mean"]) for mean in item["meanList"] ],
            "pinyin": remove_html_tags(item["pinyin"]),
        }
        ret.append(card)

    return ret[0: num]


def remove_html_tags(text):
    """
    remove html tags from soup and return TEXT

    e.g.)
        input:
            I'm <autoLink search="easy">easy</autoLink>
        output:
            I'm easy

    :param text: text which contains tags
    :return: string
    """

    soup = BeautifulSoup(text, 'lxml')
    return soup.text

def parse_mean_extends(meanExtends):
    """

    :param meanExtends:
    e.g.)
        <related entryID='968843' pinyin='búdàn' type='0'>不但</related><related entryID='968986' pinyin='bùguāng' type='0'>不光</related>
    :return:
    String
    e.g.)
        "不但, 不光"
    """

    soup = BeautifulSoup(meanExtends, 'lxml')
    relateds = soup.find_all("related")

    return ", ".join([r.text for r in relateds])
