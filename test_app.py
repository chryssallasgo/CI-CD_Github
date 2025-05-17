import unittest
HEAD
from app import add, subtract, greet
=======
from app import add, subtract, greet, multiply
1b571d0 (Feature: Added Multiplication)

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

HEAD
if __name__ == '__main__':
  unittest.main()

  def test_multiply_positive_numbers(self):
    self.assertEqual(multiply(3, 4), 12)

  def test_multiply_with_zero(self):
    self.assertEqual(multiply(0, 5), 0)

  def test_multiply_negative_numbers(self):
    self.assertEqual(multiply(-2, -3), 6)

  def test_multiply_mixed_signs(self):
    self.assertEqual(multiply(-2, 3), -6)

if __name__ == '__main__':
  unittest.main()
1b571d0 (Feature: Added Multiplication)
