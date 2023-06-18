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

        # I do not to intercept KeyError excetptions of the underlying dict object.
        # An exception is expected in this case, and the default error should be sufficient in this case
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

        # I do not to intercept KeyError excetptions of the underlying dict object
        # An exception is expected in this case, and the default error should be sufficient in this case
        with self.assertRaises(KeyError):
            redo_map.get('a')

    def test_set_with_the_same_key(self):
        redo_map = RedoDictionary()

        redo_map.set('b', 3)
        redo_map.set('b', 5)

        redo_map.undo()
        self.assertEqual(redo_map.get('b'), 3)

    def test_redo_after_set(self):
        redo_map = RedoDictionary()

        redo_map.set('b', 3)
        redo_map.undo()
        redo_map.set('c', 4)

        # TODO: IndexError is probably is not a clear error in this case.
        # Probably should throw a custom error.

        with self.assertRaises(IndexError):
            redo_map.redo()

    def test_redo_after_delete(self):
        redo_map = RedoDictionary()

        redo_map.set('b', 3)
        redo_map.set('b', 7)
        redo_map.undo()
        redo_map.delete('b')

        # TODO: IndexError is probably is not a clear error in this case.
        # Probably should throw a custom error.

        with self.assertRaises(IndexError):
            redo_map.redo()


if __name__ == '__main__':
    unittest.main()
