from django.test import TestCase
from string_calculator.views import StringCalculator

class StringCalculatorTests(TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_add_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_add_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_add_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)

    def test_add_numbers_with_newline(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
        self.assertEqual(self.calculator.add("1\n2\n3"), 6)

    def test_add_with_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_add_with_negative_number(self):
        with self.assertRaises(Exception) as context:
            self.calculator.add("1,-2,3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

    def test_add_with_multiple_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            self.calculator.add("1,-2,-3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -3")

    def test_subtract_multiple_numbers(self):
        self.assertEqual(self.calculator.subtract("5,2,1"), 2)  # 5 - 2 - 1 = 2

    def test_subtract_no_numbers(self):
        self.assertEqual(self.calculator.subtract(""), 0)  # Default case, should be 0

    def test_subtract_single_number(self):
        self.assertEqual(self.calculator.subtract("5"), 5)  # 5 - 0 = 5

    def test_multiply_multiple_numbers(self):
        self.assertEqual(self.calculator.multiply("2,3,4"), 24)  # 2 * 3 * 4 = 24

    def test_multiply_no_numbers(self):
        self.assertEqual(self.calculator.multiply(""), 1)  # Default case, should be 1

    def test_multiply_single_number(self):
        self.assertEqual(self.calculator.multiply("5"), 5)  # 5 * 1 = 5

    def test_divide_multiple_numbers(self):
        self.assertEqual(self.calculator.divide("12,3,2"), 2)  # 12 / 3 / 2 = 2

    def test_divide_no_numbers(self):
        self.assertEqual(self.calculator.divide(""), 0)  # Default case, should be 0

    def test_divide_single_number(self):
        self.assertEqual(self.calculator.divide("10"), 10)  # 10 / 1 = 10

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            self.calculator.divide("10,0")
        self.assertEqual(str(context.exception), "Division by zero is not allowed")
