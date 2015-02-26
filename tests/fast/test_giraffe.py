import unittest
import random

__author__ = 'cathywu'

class TestGiraffe(unittest.TestCase):
    def setUp(self):
        # The setup code is run before each test
        self.seed = 237423433

    def test_true(self):
        # Dummy test
        self.assertTrue(True)

    def test_height(self):
        # This tests that the random number is 4
        from boilerplate.Giraffe import Giraffe 
        g = Giraffe(seed=self.seed)
        self.assertTrue(g.height == 7)

if __name__ == '__main__':
    unittest.main()
