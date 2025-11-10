import unittest
from unittest.mock import Mock, MagicMock, patch
from compIntCalc import *
import pytest

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if results correct
    def test_days(self):
        self.assertEqual(comp_in_calc(800, 0.05, 24), 882.0)


# TESTING ERROR TESTING FOR INITIAL SAVINGS AMOUNT FUNCTION

        #checks savings will reject non numeric values
    def tests_non_numeric_savings(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_non_numeric):
                initial_savings_amount()

        #checks savings will reject negative values
    def tests_value_min_value_savings(self):
        with patch("builtins.input", return_value="-1"):
            with pytest.raises(ValueError, match = prompt_error_handling_negative):
                initial_savings_amount()
    
     #checks savings will reject numbers over 2 dp
    def tests_value_2_dp(self):
        with patch("builtins.input", return_value="800.577"):
            with pytest.raises(ValueError, match = prompt_error_handling_dp):
                initial_savings_amount()




# make sure user cant input value greater than 7 for days

#i wanna add a try thingy so maybe a self.assert(equal) to an error message of "Insert a number no larger than (days)"

    # run the tests
if __name__ == "__main__":
    unittest.main()



