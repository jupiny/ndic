#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from ndic import ndic 


class NdicTestCase(TestCase):

    def test_ndic_should_return_english_word_corresponding_to_korean_word(self):
        test_search_korean_word = "사과"
        test_corresponding_english_word = "(과일) apple"
        self.assertEqual(
            ndic(test_search_korean_word),
            test_corresponding_english_word,
        )

    def test_ndic_should_return_korean_word_corresponding_to_english_word(self):
        test_search_english_word = "apple"
        test_corresponding_korean_word = "사과"
        self.assertEqual(
            ndic(test_search_english_word),
            test_corresponding_korean_word,
        )
    
    def test_ndic_should_return_empty_string_if_nonexistent_korean_word(self):
        test_nonexistent_korean_word = "아갸야라"
        self.assertFalse(
            ndic(test_nonexistent_korean_word),
        )

    def test_ndic_should_return_empty_string_if_nonexistent_english_word(self):
        test_nonexistent_english_word = "asfasdfasdf"
        self.assertFalse(
            ndic(test_nonexistent_english_word),
        )
