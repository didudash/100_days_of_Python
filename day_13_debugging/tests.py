import unittest
from unittest.mock import patch
from io import StringIO
from main import odd_or_even, leap_year, fizzbuzz

class TestDebuggingExamples(unittest.TestCase):

    def test_odd_or_even_even(self):
        with patch('builtins.input', return_value="2"), \
             patch('builtins.print') as mock_print:
            odd_or_even()
        mock_print.assert_called_with("This is an even number.")

    def test_odd_or_even_odd(self):
        with patch('builtins.input', return_value="3"), \
             patch('builtins.print') as mock_print:
            odd_or_even()
        mock_print.assert_called_with("This is an odd number.")

    def test_leap_year_leap(self):
        with patch('builtins.input', return_value="2000"), \
             patch('builtins.print') as mock_print:
            leap_year()
        mock_print.assert_called_with("Leap year.")

    def test_leap_year_not_leap(self):
        with patch('builtins.input', return_value="1900"), \
             patch('builtins.print') as mock_print:
            leap_year()
        mock_print.assert_called_with("Not leap year.")

    def test_fizzbuzz(self):
        expected_output = "\n".join([
            "1", "2", "Fizz", "4", "Buzz", 
            "Fizz", "7", "8", "Fizz", "Buzz", 
            "11", "Fizz", "13", "14", "FizzBuzz"
        ])
        with patch('builtins.input', return_value="15"), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            fizzbuzz()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()
