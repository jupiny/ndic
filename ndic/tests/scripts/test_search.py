# -*- coding: utf-8 -*-
from unittest import TestCase

from click.testing import CliRunner
import mock
import requests

from ndic.scripts.search import cli_search
from ndic.exceptions import NdicConnectionError


class NdicScriptTestCase(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_search_korean_word(self):
        result = self.runner.invoke(
            cli_search,
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
            cli_search,
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
            cli_search,
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
            cli_search,
            ["asfasdfasdf"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertFalse(
            result.output.replace('\n', ''),
        )

    def test_search_korean_word_multiple_meaning(self):
        test_corresponding_english_word_1 = u"(언어) word, language, speech, " \
                                            "(literary) tongue"
        test_corresponding_english_word_2 = u"(동물) horse"
        test_corresponding_english_word_3 = u"(마지막) end (of), close (of)"

        result1 = self.runner.invoke(
            cli_search,
            ["말", "-x", "1"],
        )
        self.assertEqual(
            result1.exit_code,
            0,
        )
        self.assertEqual(
            result1.output.replace('\n', ''),
            test_corresponding_english_word_1,
        )

        result2 = self.runner.invoke(
            cli_search,
            ["말", "--xth", "2"],
        )
        self.assertEqual(
            result2.exit_code,
            0,
        )
        self.assertEqual(
            result2.output.replace('\n', ''),
            test_corresponding_english_word_2,
        )

        result3 = self.runner.invoke(
            cli_search,
            ["말", "-x", "3"],
        )
        self.assertEqual(
            result3.exit_code,
            0,
        )
        self.assertEqual(
            result3.output.replace('\n', ''),
            test_corresponding_english_word_3,
        )

    def test_search_english_word_multiple_meaning(self):
        test_corresponding_korean_word_1 = u"받다"
        test_corresponding_korean_word_2 = u"얻다, 입수하다; 가지다(obtain)"
        test_corresponding_korean_word_3 = u"(동물의) 새끼; 새끼를 낳음"

        result1 = self.runner.invoke(
            cli_search,
            ["get", "-x", "1"],
        )
        self.assertEqual(
            result1.exit_code,
            0,
        )
        self.assertEqual(
            result1.output.replace('\n', ''),
            test_corresponding_korean_word_1,
        )

        result2 = self.runner.invoke(
            cli_search,
            ["get", "--xth", "2"],
        )
        self.assertEqual(
            result2.exit_code,
            0,
        )
        self.assertEqual(
            result2.output.replace('\n', ''),
            test_corresponding_korean_word_2,
        )

        result3 = self.runner.invoke(
            cli_search,
            ["get", "-x", "3"],
        )
        self.assertEqual(
            result3.exit_code,
            0,
        )
        self.assertEqual(
            result3.output.replace('\n', ''),
            test_corresponding_korean_word_3,
        )

    def test_search_xth_exceed(self):
        result = self.runner.invoke(
            cli_search,
            ["말", "-x", "10"],
        )
        self.assertEqual(
            result.exit_code,
            0,
        )
        self.assertFalse(
            result.output.replace('\n', ''),
        )

    def test_search_negative_or_zero_xth(self):
        result1 = self.runner.invoke(
            cli_search,
            ["말", "-x", "0"],
        )
        self.assertEqual(
            result1.exit_code,
            0,
        )
        self.assertFalse(
            result1.output.replace('\n', ''),
        )

        result2 = self.runner.invoke(
            cli_search,
            ["말", "-x", "-1"],
        )
        self.assertEqual(
            result2.exit_code,
            0,
        )
        self.assertFalse(
            result2.output.replace('\n', ''),
        )

    @mock.patch.object(requests, 'get', side_effect=requests.ConnectionError)
    def test_search_without_internet_network(self, mock_requests):
        result = self.runner.invoke(
            cli_search,
            ["사과"],
        )
        self.assertEqual(
            result.exit_code,
            1,
        )
        self.assertEqual(
            result.exception.__class__,
            NdicConnectionError,
        )
        self.assertEqual(
            str(result.exception),
            str(NdicConnectionError()),
        )
        self.assertEqual(
            repr(result.exception),
            repr(NdicConnectionError()),
        )
