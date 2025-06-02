import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_simple_operations(self):
        self.assertEqual(self.calc.calculate("2 + 2"), 4)
        self.assertEqual(self.calc.calculate("5 - 3"), 2)
        self.assertEqual(self.calc.calculate("4 * 3"), 12)
        self.assertEqual(self.calc.calculate("10 / 2"), 5)

    def test_operator_precedence(self):
        self.assertEqual(self.calc.calculate("2 + 3 * 4"), 14)
        self.assertEqual(self.calc.calculate("(2 + 3) * 4"), 20)
        self.assertEqual(self.calc.calculate("10 - 4 / 2"), 8)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate("5 / 0")

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            self.calc.calculate("2 +")
        with self.assertRaises(ValueError):
            self.calc.calculate("(2 + 3")
        with self.assertRaises(ValueError):
            self.calc.calculate("2 & 3")



if __name__ == '__main__':
    unittest.main()