import unittest
from coding_practice import chapter_1 as ch1


class TestChapter1(unittest.TestCase):

    def test_exc1_is_unique_1(self):
        self.assertTrue(ch1.exc1_is_unique_1('abcde'), 'Input is unique.')
        self.assertFalse(ch1.exc1_is_unique_1('aabcde'), 'Input is not unique.')
        self.assertTrue(ch1.exc1_is_unique_1(''), 'Empty string should be unique.')
        self.assertFalse(ch1.exc1_is_unique_1('aaaaa'), 'Input not unique.')

    def test_exc2_check_permutation(self):
        for permutation_func in [ch1.exc2_check_permutation, ch1.exc2_check_permutation_2]:
            self.assertTrue(permutation_func('abc', 'bca'), 'Strings are permutations of each other.')
            self.assertTrue(permutation_func('aa', 'aa'), 'Strings are permutations of each other.')
            self.assertTrue(permutation_func('', ''), 'Two empty strings are the same.')
            self.assertFalse(permutation_func('', 'a'), 'Empty string cannot be permuted.')
            self.assertFalse(permutation_func('abc', 'bce'), 'No permutations.')

    def test_exc3_urlify(self):
        self.assertEqual(ch1.exc3_urlify('Mr John Smith     ', 13), 'Mr%20John%20Smith')

    def test_exc4_palindrome_permutation(self):
        test_cases = [('Tact Coa', True),
                      ('Anan', True),
                      ('a', True),
                      ('', True),
                      ('abc', False),
                      ('aaab', False)]
        for input_string, expected_result in test_cases:
            self.assertEqual(ch1.exc4_palindrome_permutation(input_string), expected_result,
                             f'Test case {input_string} failed - should be {expected_result}!')

    def test_exc5_one_away(self):
        test_cases = [('baker', 'bakers', True), ('baker', 'baakker', False),  # insert
                      ('baker', 'baer', True),   ('baker', 'bkr', False),      # remove
                      ('baker', 'backer', True), ('baker', 'bxkyr', False)     # replace
                      ]

        for str1, str2, expected_result in test_cases:
            self.assertEqual(expected_result, ch1.exc5_one_away(str1, str2),
                             f'Test case ({str1}, {str2}) failed, should be: {expected_result}')

    def test_exc6_string_compression(self):
        test_cases = [('aabcccccaaa', 'a2b1c5a3'),
                      ('abcd', 'abcd'),
                      ('a', 'a'),
                      ('', ''),
                      (' ', ' ')]
        for test_idx, (input_str, expected_result) in enumerate(test_cases):
            with self.subTest(test=test_idx + 1):
                self.assertEqual(expected_result, ch1.exc6_string_compression(input_str))
