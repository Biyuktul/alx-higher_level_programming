import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntClass(unittest.TestCase):
    def test_max_integer(self):
        # max_integer functionality test
        self.assertEqual(max_integer([2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-2, -3, -4, -1, -5]), -1)
        self.assertEqual(max_integer([20, -3, -4, -1, -5]), 20)
