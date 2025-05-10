import unittest
from app import add, subtract, greet

class TestApp(unittest.TestCase):

  def test_add_positive_numbers(self):
    self.assertEqual(add(2, 3), 5)

  def test_add_negative_numbers(self):
    self.assertEqual(add(-1, -4), -5)

  def test_subtract_positive_numbers(self):
    self.assertEqual(subtract(5, 2), 3)

  def test_subtract_negative_numbers(self):
    self.assertEqual(subtract(-5, -2), -3)

  def test_greet_with_name(self):
    self.assertEqual(greet("Alice"), "Hello, Alice!")

  def test_greet_with_empty_name(self):
    self.assertEqual(greet(""), "Hello, !")

if __name__ == '__main__':
  unittest.main()