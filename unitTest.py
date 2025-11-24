import unittest
from unittest.mock import Mock, MagicMock, patch
from mainCode import *
import pytest

# define the unit tests
class my_unit_tests(unittest.TestCase):


# ---------------------------------------------------------------------
# TESTING: initial_savings_amount()
# ---------------------------------------------------------------------

    # Tests to see if function takes correct values
    def test_valid_savings(self):
        with patch("builtins.input", return_value="800.57"):
            result = initial_savings_amount()
            assert result == 800.57

    # Tests to see if users can pass in strings
    def test_string_savings(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_non_numeric):
                initial_savings_amount()

    # Tests to see if users can pass in negative values
    def tests_value_min_value_savings(self):
        with patch("builtins.input", return_value="-1"):
            with pytest.raises(ValueError, match = prompt_error_handling_negative):
                initial_savings_amount()

    # Tests to see if users can pass in values over 2 decimal places
    def tests_value_2_dp(self):
        with patch("builtins.input", return_value="800.577"):
            with pytest.raises(ValueError, match = prompt_error_handling_dp):
                initial_savings_amount()

# ---------------------------------------------------------------------
# TESTING: rate()
# ---------------------------------------------------------------------

    # Tests to see if function takes correct values
    def test_valid_rate(self):
        with patch("builtins.input", return_value="0.05"):
            result = rate()
            assert result == 0.05

    # Tests to see if users can pass in strings
    def tests_string_rate(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_non_numeric):
                rate()

    # Tests to see if users can pass in negative values
    def tests_value_min_value_rate(self):
        with patch("builtins.input", return_value="-1"):
            with pytest.raises(ValueError, match = prompt_error_handling_rate):
                rate()             

    # Tests to see if users can pass in values above 1
    def tests_value_max_value_rate(self):
        with patch("builtins.input", return_value="1.1"):
            with pytest.raises(ValueError, match = prompt_error_handling_rate):
                rate()             

# ---------------------------------------------------------------------
# TESTING:  time()
# ---------------------------------------------------------------------

    # Tests to see if function takes correct values
    def test_valid_time(self):
        with patch("builtins.input", return_value="12"):
            result = time()
            assert result == 12

    # Tests to see if users can pass in strings
    def tests_string_time(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_non_numeric):
                time()

    # Tests to see if users can pass in negative values
    def tests_value_min_value_time(self):
        with patch("builtins.input", return_value="-1"):
            with pytest.raises(ValueError, match = prompt_error_handling_negative):
                time()             

    # Tests to see if users can pass in floats
    def tests_value_float_time(self):
        with patch("builtins.input", return_value="1.1"):
            with pytest.raises(ValueError, match = prompt_error_handling_non_numeric):
                time()             

# ---------------------------------------------------------------------
# TESTING:  comp_in_calc()
# ---------------------------------------------------------------------

    # Tests if results produced correct
    def test_days(self):
        self.assertEqual(comp_in_calc(800, 0.05, 24), 882.0)


    # run the tests
if __name__ == "__main__":
    unittest.main()



