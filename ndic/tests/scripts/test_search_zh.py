# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner

from ndic.scripts.search import cli_search_zh

import re


class NdicZhCliTest(unittest.TestCase):
    """
        Test ndic's chinese search works on cli environment
    """

    def setUp(self):
        self.runner = CliRunner()

    @classmethod
    def remove_white_space(cls, output):
        return re.sub(r"[^w]", "", output)

    def test_search_with_one_num(self):
        result = self.runner.invoke(cli_search_zh, ["你好", "--number", "1"])
        expected_result = """
        你好(nǐhǎo)
        안녕하십니까? 
        """
        self.assertEqual(
            self.remove_white_space(result.output),
            self.remove_white_space(expected_result),
        )

    def test_search_with_num_two(self):
        result = self.runner.invoke(cli_search_zh, ["你好", "--number", "2"])
        expected_result = """
        你好(nǐhǎo)
        안녕하십니까? 
        
        你好吗(nǐhǎoma)
        안녕하십니까? 안녕하세요?
        """
        self.assertEqual(
            self.remove_white_space(result.output),
            self.remove_white_space(expected_result),
        )

    def test_search_with_num_three(self):
        input = "快乐"
        result = self.runner.invoke(cli_search_zh, [input, "-n", "3"])
        expected_result = """
        快乐(kuàilè)
        즐겁다. 유쾌하다. 
        
        快乐的(kuàilède)
        행복한. 
        
        快乐地(kuàilède)
        행복하게. 
        """
        self.assertEqual(
            self.remove_white_space(result.output),
            self.remove_white_space(expected_result),
        )

    def test_nonexistent_word(self):
        """
        no use to test this

        because naver always returns the most similar word's result
        """
        pass


if __name__ == '__main__':
    unittest.main()
