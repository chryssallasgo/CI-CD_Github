import unittest
from app import add, subtract, multiply, divide, greet

class TestApp(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -2), -3)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_with_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_default(self):
        self.assertEqual(greet(), "Hello, Guest!")

    def test_greet_title_case(self):
        self.assertEqual(greet("bob"), "Hello, Bob!")

if __name__ == '__main__':
    unittest.main()
