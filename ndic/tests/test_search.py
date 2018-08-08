# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from unittest import TestCase

import mock
import requests

from ndic.search import search
from ndic.exceptions import NdicConnectionError


class NdicTestCase(TestCase):

    def test_search_korean_word(self):
        test_search_korean_word = "사과"
        test_corresponding_english_word = "(과일) apple"
        self.assertEqual(
            search(test_search_korean_word),
            test_corresponding_english_word,
        )

    def test_search_english_word(self):
        test_search_english_word = "apple"
        test_corresponding_korean_word = "사과"
        self.assertEqual(
            search(test_search_english_word),
            test_corresponding_korean_word,
        )

    def test_search_nonexistent_korean_word(self):
        test_nonexistent_korean_word = "아갸야라"
        self.assertFalse(
            search(test_nonexistent_korean_word),
        )

    def test_search_nonexistent_english_word(self):
        test_nonexistent_english_word = "asfasdfasdf"
        self.assertFalse(
            search(test_nonexistent_english_word),
        )

    def test_search_korean_word_multiple_meaning(self):
        test_search_korean_word = "말"
        test_corresponding_english_word_1 = "(언어) word, language, speech, " \
                                            "(literary) tongue"
        test_corresponding_english_word_2 = "(동물) horse"
        test_corresponding_english_word_3 = "(마지막) end (of), close (of)"
        self.assertEqual(
            search(test_search_korean_word, 1),
            test_corresponding_english_word_1,
        )
        self.assertEqual(
            search(test_search_korean_word, 2),
            test_corresponding_english_word_2,
        )
        self.assertEqual(
            search(test_search_korean_word, 3),
            test_corresponding_english_word_3,
        )

    def test_search_english_word_multiple_meaning(self):
        test_search_english_word = "get"
        test_corresponding_korean_word_1 = "받다"
        test_corresponding_korean_word_2 = "얻다, 입수하다; 가지다(obtain)"
        test_corresponding_korean_word_3 = "(동물의) 새끼; 새끼를 낳음"
        self.assertEqual(
            search(test_search_english_word, 1),
            test_corresponding_korean_word_1,
        )
        self.assertEqual(
            search(test_search_english_word, 2),
            test_corresponding_korean_word_2,
        )
        self.assertEqual(
            search(test_search_english_word, 3),
            test_corresponding_korean_word_3,
        )

    def test_search_xth_exceed(self):
        test_nonexistent_english_word = "말"
        self.assertFalse(
            search(test_nonexistent_english_word, 10),
        )

    def test_search_negative_or_zero_xth(self):
        test_nonexistent_english_word = "말"
        self.assertFalse(
            search(test_nonexistent_english_word, -1),
        )
        self.assertFalse(
            search(test_nonexistent_english_word, 0),
        )

    @mock.patch.object(requests, 'get', side_effect=requests.ConnectionError)
    def test_search_without_internet_network(self, mock_requests):
        test_search_korean_word = "사과"
        self.assertRaises(
            NdicConnectionError,
            search,
            test_search_korean_word,
        )
