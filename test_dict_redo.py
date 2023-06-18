#!/usr/bin/env python3
import unittest
from dict_redo import RedoDictionary


class TestDictRedo(unittest.TestCase):

    def test_getting_element(self):
        redo_map = RedoDictionary()
        redo_map.set('a', 3)
        self.assertEqual(redo_map.get('a'), 3)

    def test_removal(self):
        redo_map = RedoDictionary()
        redo_map.set('a', 3)
        self.assertEqual(redo_map.get('a'), 3)

        redo_map.delete('a')
        with self.assertRaises(KeyError):
            redo_map.get('a')

    def test_undo(self):
        redo_map = RedoDictionary()

        redo_map.set('a', 3)
        redo_map.delete('a')
        redo_map.undo()

        self.assertEqual(redo_map.get('a'), 3)

    def test_redo(self):
        redo_map = RedoDictionary()

        redo_map.set('a', 3)
        redo_map.delete('a')
        redo_map.undo()
        redo_map.redo()

        with self.assertRaises(KeyError):
            redo_map.get('a')

    def test_set_with_the_same_key(self):
        redo_map = RedoDictionary()

        redo_map.set('b', 3)
        redo_map.set('b', 5)

        redo_map.undo()
        self.assertEqual(redo_map.get('b'), 3)


if __name__ == '__main__':
    unittest.main()
