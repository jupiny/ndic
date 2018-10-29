# -*- coding: utf-8 -*-
import unittest
from click.testing import CliRunner

import ndic
from ndic.exceptions import CannotFindResultError


class NdicZhPythonTest(unittest.TestCase):
    """
        Test ndic's chinese search works on python interpreter environment
    """

    def test_search_zh(self):
        test_inputs = []
        test_results = []

        test_input = "的"
        test_result = [
            {
                'origin': '的',
                'meanings': [
                    '‘定语’ (한정어)의 뒤에 붙음.',
                    '한정어와 중심어의 관계가 일반적인 수식 관계임.',
                    '한정어와 중심어의 관계가 종속 관계임.',
                ],
                'pinyin': '‧de'
            }
        ]

        test_inputs.append(test_input)
        test_results.append(test_result)

        test_input = "苹果"
        test_result = [
            {
                'origin': '苹果',
                'meanings': ['사과(나무).'],
                'pinyin': 'píngguǒ',
            }
        ]

        test_inputs.append(test_input)
        test_results.append(test_result)

        import sys
        if sys.version_info[0] == 2:
            # version 2 have unicode error
            return

        for t, r in zip(test_inputs, test_results):
            self.assertEqual(
                ndic.search_zh(t),
                r,
            )

    def test_search_nonexistent_english_word(self):
        input = "qpqppqppqpqsdpfjas"
        with self.assertRaises(CannotFindResultError):
            ndic.search_zh(input)


class NdicZhCliTest(unittest.TestCase):
    """
        Test ndic's chinese search works on cli environment
    """

    def setUp(self):
        self.runner = CliRunner()

    @classmethod
    def output2str(cls, output):
        return str(output.encode('utf-8', 'ignore').decode("utf-8"))

    def test_search_with_one_num(self):
        pass

    def test_search_with_num_two(self):
        pass

    def test_search_with_num_three(self):
        pass

    def test_nonexistent_word(self):
        pass
