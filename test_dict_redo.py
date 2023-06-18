#!/usr/bin/env python3
import unittest
from dict_redo import RedoDictionary

class TestDictRedo(unittest.TestCase):
    def test_one_test_to_rule_them_all(self):
        # TODO: Split the test

        our_dict = RedoDictionary()

        our_dict.add('a', 3)
        assert our_dict.get('a') == 3

        our_dict.remove('a')
        # assert our_dict.get('a') == 3

        our_dict.undo()
        assert our_dict.get('a') == 3

        our_dict.redo()
        # assert our_dict.get('a') == 3

        our_dict.undo()
        assert our_dict.get('a') == 3

        our_dict.add('b', 3)
        our_dict.add('b', 5)
        our_dict.undo()
        assert our_dict.get('b') == 3


if __name__ == '__main__':
    unittest.main()
