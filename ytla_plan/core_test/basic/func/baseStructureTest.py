# coding=utf-8
import unittest
from core.basic.func.baseStructure import (
    str_to_dict,
    str_to_list,
    str_to_tuple,
    add_count_for_dict,
    set_pick
)


class TestBaseStructureFunctions(unittest.TestCase):
    """Unit tests for base structure manipulation functions."""

    def test_str_to_dict_valid_input(self):
        """Should correctly convert well-formatted dictionary string."""
        test_str = "{'name': 'John', 'age': 30}"
        result = str_to_dict(test_str)
        self.assertEqual(result, {'name': 'John', 'age': 30})

    def test_str_to_list_conversion(self):
        """Should convert string to list of characters."""
        self.assertEqual(str_to_list("abc"), ['a', 'b', 'c'])
        self.assertEqual(str_to_list("123"), ['1', '2', '3'])

    def test_str_to_tuple_conversion(self):
        """Should convert string to tuple of characters."""
        self.assertEqual(str_to_tuple("xyz"), ('x', 'y', 'z'))
        self.assertEqual(str_to_tuple("456"), ('4', '5', '6'))

    def test_add_count_for_dict_new_key(self):
        """Should initialize count for new dictionary key."""
        test_dict = {}
        result = add_count_for_dict('counter', test_dict, 5)
        self.assertEqual(result['counter'], 5)

    def test_add_count_for_dict_existing_key(self):
        """Should increment count for existing dictionary key."""
        test_dict = {'counter': 10}
        result = add_count_for_dict('counter', test_dict, 3)
        self.assertEqual(result['counter'], 13)

    def test_set_pick_filtering(self):
        """Should filter elements not in base or exclude lists."""
        check = [1, 2, 3, 4]
        base = [2, 5]
        exclude = [3]
        self.assertEqual(set_pick(check, base, exclude), [1, 4])

    def test_set_pick_empty_lists(self):
        """Should handle empty input lists correctly."""
        self.assertEqual(set_pick([], [1], [2]), [])
        self.assertEqual(set_pick([1, 2], [], []), [1, 2])


if __name__ == '__main__':
    unittest.main()
