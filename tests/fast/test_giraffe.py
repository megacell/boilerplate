import unittest
import random

__author__ = 'cathywu'

class TestGiraffe(unittest.TestCase):
    def setUp(self):
        # The setup code is run before each test
        seed = 237423433
        random.seed(seed)

    def test_true(self):
        # Dummy test
        self.assertTrue(True)

    def test_height(self):
        # This tests that the random number is 4
        from boilerplate.giraffe import Giraffe 
        g = Giraffe()
        self.assertTrue(g.height == 7)

if __name__ == '__main__':
    unittest.main()
