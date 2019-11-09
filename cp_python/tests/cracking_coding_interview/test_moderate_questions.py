import unittest

from cracking_coding_interview.moderate_questions import *
from tests.test_utils import run_sub_tests


class TestModerateQuestions(unittest.TestCase):
    def test_word_frequencies(self):
        book = 'This is my book. My book is awesome.'
        book = ''.join([char for char in book if char is not '.']).split(' ')
        output = {'this': 1, 'is': 2, 'my': 2, 'book': 2, 'awesome': 1}
        self.assertEqual(output, exc_16_2_word_frequencies(book))

    def test_intersection(self):
        # TODO: test for actual intersectino points not only if intersection has been found or not.
        # Test where the lines intersect
        start1, end1 = Point(1, 1), Point(3, 3)
        start2, end2 = Point(0, 2), Point(2, 1)
        self.assertIsNotNone(exc_16_3_intersection(start1, end1, start2, end2))

        # Test where the lines have different slopes but do not intersect within their domains
        start1, end1 = Point(1, 1), Point(2, 2)
        start2, end2 = Point(2, 1), Point(3, 3)
        self.assertIsNone(exc_16_3_intersection(start1, end1, start2, end2))

        # Test where they have the same slope but no domain overlap
        start1, end1 = Point(1, 1), Point(2, 2)
        start2, end2 = Point(3, 3), Point(4, 4)
        self.assertIsNone(exc_16_3_intersection(start1, end1, start2, end2))

        # Test where they have the same slope and domain overlap
        start1, end1 = Point(1, 1), Point(3, 3)
        start2, end2 = Point(2, 2), Point(4, 4)
        self.assertIsNotNone(exc_16_3_intersection(start1, end1, start2, end2))


if __name__ == '__main__':
    unittest.main()
