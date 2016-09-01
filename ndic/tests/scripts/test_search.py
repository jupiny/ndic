# -*- coding: utf-8 -*-
from unittest import TestCase

from click.testing import CliRunner

from ndic.scripts import ndic


class NdicScriptTestCase(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_search_korean_word(self):
        result = self.runner.invoke(
            ndic.search,
            ["사과"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertEqual(
            result.output.replace('\n', ''),
            u"(과일) apple",
        )

    def test_search_english_word(self):
        result = self.runner.invoke(
            ndic.search,
            ["apple"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertEqual(
            result.output.replace('\n', ''),
            u"사과",
        )

    def test_search_nonexistent_korean_word(self):
        result = self.runner.invoke(
            ndic.search,
            ["아갸야라"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertFalse(
            result.output.replace('\n', ''),
        )

    def test_search_nonexistent_english_word(self):
        result = self.runner.invoke(
            ndic.search,
            ["asfasdfasdf"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertFalse(
            result.output.replace('\n', ''),
        )
