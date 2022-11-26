import unittest

from src.exercise.standard_exercise import ModThree


class TestModThree(unittest.TestCase):

    def test_mod_three_valid_input_one(self):
        mod = ModThree()
        actual = mod.mod_three("1101")
        expected = 1
        self.assertEqual(expected, actual)

    def test_mod_three_valid_input_two(self):
        mod = ModThree()
        actual = mod.mod_three("1110")
        expected = 2
        self.assertEqual(expected, actual)

    def test_mod_three_valid_input_three(self):
        mod = ModThree()
        actual = mod.mod_three("1111")
        expected = 0
        self.assertEqual(expected, actual)

    def test_mod_three_valid_input_four(self):
        mod = ModThree()
        actual = mod.mod_three("110")
        expected = 0
        self.assertEqual(expected, actual)

    def test_mod_three_valid_input_five(self):
        mod = ModThree()
        actual = mod.mod_three("1010")
        expected = 1
        self.assertEqual(expected, actual)

    def test_mod_three_valid_input_six(self):
        mod = ModThree()
        actual = mod.mod_three("")
        expected = 0
        self.assertEqual(expected, actual)

    def test_mod_three_valid_input_seven(self):
        mod = ModThree()
        actual = mod.mod_three("1")
        expected = 1
        self.assertEqual(expected, actual)

    def test_mod_three_invalid_input_one(self):
        mod = ModThree()
        actual = mod.mod_three("1a010")
        expected = None
        self.assertEqual(expected, actual)

    def test_mod_three_invalid_input_two(self):
        mod = ModThree()
        actual = mod.mod_three("012")
        expected = None
        self.assertEqual(expected, actual)

    def test_mod_three_invalid_input_type(self):
        mod = ModThree()
        actual = mod.mod_three(1010)
        expected = None
        self.assertEqual(expected, actual)

    def test_mod_three_invalid_input_str_length(self):
        mod = ModThree()
        actual = mod.mod_three("101010101010101010101010")
        expected = None
        self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()
