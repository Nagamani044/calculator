import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(divide(10, 0), 5)  # This test will raise an error

if _name_ == '_main_':
    unittest.main()