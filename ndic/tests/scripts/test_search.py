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

    @mock.patch.object(requests, 'get', side_effect=requests.ConnectionError)
    def test_search_without_internet_network(self, mock_requests):
        result = self.runner.invoke(
            cli_search,
            ["사과"],
        )
        self.assertEqual(
            result.exit_code,
            -1,
        )
        self.assertEqual(
            result.exception.__class__,
            NdicConnectionError,
        )
        self.assertEqual(
            str(result.exception),
            str(NdicConnectionError()),
        )
