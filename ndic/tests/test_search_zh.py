import unittest

import ndic
from ndic.exceptions import CannotFindResultError

class NdicZhPythonTest(unittest.TestCase):
    """
        Test ndic's chinese search
    """

    @classmethod
    def output2str(cls, output):
        return str(output.encode('utf-8', 'ignore').decode("utf-8"))

    def test_search_zh(self):
        test_search_chinese_word = "随便"
        test_result = """
        -------------------------\n随便(suí//biàn)\n[동사] 마음대로(좋을대로, 형편대로) 하다. \n-------------------------\n随便(suíbiàn)\n[부사] 마음대로. 좋을대로. 자유로이. 함부로. 제멋대로. \n[형용사] 무책임하다. 부주의하다. 함부로 하다. 제멋대로 하다. \n[반의어] 郑重(zhèngzhòng) \n[접속사] …을 막론하고. …라 할 것 없이. \n-------------------------\n随便的(suíbiànde)\n막 대하는. \n-------------------------\n随便地(suíbiànde)\n막 대하며. \n-------------------------\n我随便(Wǒ suíbiàn)\nI'm easy \n
        """.strip()
        self.assertEqual(
            ndic.search_zh(test_search_chinese_word).strip(),
            self.output2str(test_result)
        )

    def test_search_nonexisting_english_word(self):
        src = "qpqppqppqpqsdpfjas"
        with self.assertRaises(CannotFindResultError):
            ndic.search_zh(src)

if __name__ == '__main__':
    unittest.main()
