# -*- coding: utf-8 -*-

"""
This module provides constants that are used within Ndic

"""
from __future__ import unicode_literals


NAVER_ENDIC_URL = "http://endic.naver.com/search.nhn?"\
    + "sLn=kr&searchOption=all&query={search_word}"

NAVER_ZHDIC_URL = "https://zh.dict.naver.com/cndictApi/search/all?"\
    + "sLn=undefined&mode=pc&pageNo=1&format=json&q={search_word}"

CONNECTION_ERROR_MESSAGE = "Network connection is lost. "\
    + "Please check the connection to the Internet."

CANNOT_FIND_RESULT_MESSAGE = "Sorry We Didn't Find Any Results Matching This Search"\
    + "Please recheck your input is valid"
