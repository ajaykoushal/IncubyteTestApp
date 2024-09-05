from django.test import TestCase
from .views import StringCalculator


class StringCalculatorTests(TestCase):
    
    def setUp(self):
        self.calculator = StringCalculator()

    def test_add_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_add_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_add_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3"), 6)
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
        self.assertEqual(self.calculator.add("1\n2\n3"), 6)

    def test_add_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2;3"), 6)

    def test_add_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            self.calculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")
    
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.calculator.add("1,a,3")
