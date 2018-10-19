# -*- coding: utf-8 -*-
import unittest

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
                'meanings': [ '사과(나무).' ],
                'pinyin': 'píngguǒ',
            }
        ]

        test_inputs.append(test_input)
        test_results.append(test_result)

        for t, r in zip(test_inputs, test_results):
            self.assertEqual(
                ndic.search_zh(t),
                r,
            )

    def test_which_has_related_info(self):
        test_inputs = []
        test_results = []

        test_input = "遇见"
        test_output = [
            {
                'origin': '遇见',
                'meanings': [ '만나다. 조우(遭遇)하다.' ],
                'pinyin': 'yù//‧jiàn'
            }
        ]

        test_inputs.append(test_input)
        test_results.append(test_output)

        test_input = "兄弟"
        test_output = [
            {
                'origin': '兄弟',
                'meanings': [
                    '아우. 동생.',
                    '동생. 젊은이. 자기보다 나이 어린 남자를 친근하게 부르는 말.',
                    '저. (남자가) 자기 동년배에게나 뭇사람들 앞에서 자신을 낮추어 하는 말.',
                ],
                'pinyin': 'xiōng‧di',
            }
        ]

        test_inputs.append(test_input)
        test_results.append(test_output)

        for t, r in zip(test_inputs, test_results):
            self.assertEqual(
                ndic.search_zh(t),
                r,
            )


    def test_search_nonexistent_english_word(self):
        input = "qpqppqppqpqsdpfjas"
        with self.assertRaises(CannotFindResultError):
            ndic.search_zh(input)

from click.testing import CliRunner

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



if __name__ == '__main__':
    unittest.main()
