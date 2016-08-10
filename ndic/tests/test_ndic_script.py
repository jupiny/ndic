#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from click.testing import CliRunner

from ndic.scripts.ndic import ndic as ndic_script


class NdicScriptTestCase(TestCase):
    
    def setUp(self):
        self.runner = CliRunner()

    def test_ndic_script_should_return_english_word_corresponding_to_korean_word(self):
        result = self.runner.invoke(
            ndic_script,
            ["사과"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertEqual(
            result.output.replace('\n', ''),
            "(과일) apple",
        )

    def test_ndic_script_should_return_korean_word_corresponding_to_english_word(self):
        result = self.runner.invoke(
            ndic_script,
            ["apple"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertEqual(
            result.output.replace('\n', ''),
            "사과",
        )
    
    def test_ndic_script_should_return_empty_string_if_nonexistent_korean_word(self):
        result = self.runner.invoke(
            ndic_script,
            ["아갸야라"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertFalse(
            result.output.replace('\n', ''),
        )

    def test_ndic_script_should_return_empty_string_if_nonexistent_english_word(self):
        result = self.runner.invoke(
            ndic_script,
            ["asfasdfasdf"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertFalse(
            result.output.replace('\n', ''),
        )
