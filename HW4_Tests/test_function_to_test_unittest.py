from functions_to_test import Calculator
import unittest

class TestCalculatin(unittest.TestCase):

    def test_add(self):
        result = Calculator.add(4, 5)
        self.assertEqual(result, 9)

    def test_multiply(self):
        result = Calculator.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_subtract(self):
        result = Calculator.subtract(4, 1)
        self.assertEqual(result, 3)

    def test_divide(self):
        result = Calculator.divide(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

        #self.assertRaises(ValueError,Calculator.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()