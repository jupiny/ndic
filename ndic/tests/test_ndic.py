# -*- coding: utf-8 -*-

from unittest import TestCase

from ndic import ndic 


class NdicTestCase(TestCase):

    def test_ndic_should_return_english_word_corresponding_to_korean_word(self):
        test_korean_word = "사과"
        self.assertIn(
            "apple",
            ndic(test_korean_word),
        )

    def test_ndic_should_return_korean_word_corresponding_to_english_word(self):
        test_english_word = "apple"
        self.assertIn(
            "사과",
            ndic(test_english_word),
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
