import unittest
from time import time

from cracking_coding_interview.chapter_8 import *


class TestExc8TripleStep(unittest.TestCase):
    def test_triple_step(self):
        self.assertEqual(4, exc1_triple_step(stair_size=3))
        self.assertEqual(7, exc1_triple_step(stair_size=4))
        self.assertEqual(4, exc1_triple_step_no_global(stair_size=3))
        self.assertEqual(7, exc1_triple_step_no_global(stair_size=4))
        self.assertEqual(4, exc1_triple_step_top_down_memo(stair_size=3))
        self.assertEqual(7, exc1_triple_step_top_down_memo(stair_size=4))

        """
        # Checking if the different implementations yield same results and checking that
        # memoization solution is much, much quicker
        for i in range(24, 30):
            start = time()
            print(f'{i}: {exc1_triple_step_no_global(i)}')
            print(f'Took {time() - start}s')
            start = time()
            print(f'{i}: {exc1_triple_step(i)}')
            print(f'Took {time() - start}s')
            start = time()
            print(f'{i}: {exc1_triple_step_top_down_memo(i)}')
            print(f'Took {time() - start}s')
            print('---')
        """
