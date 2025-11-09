import unittest
from unittest import mock
from unittest.mock import Mock, MagicMock, patch
import unittest.mock as mock
from compIntCalc import *
import pytest

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if results correct
    def test_days(self):
        self.assertEqual(comp_in_calc(800, 0.05, 24), 882.0)


    def tests_value_error_savings(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_handling_non_numeric):
                initial_savings_amount()

    def tests_value_min_value_savings(self):
        with patch("builtins.input", return_value="-1"):
            with pytest.raises(ValueError, match = prompt_error_handling_negative):
                initial_savings_amount()




# make sure user cant input value greater than 7 for days

#i wanna add a try thingy so maybe a self.assert(equal) to an error message of "Insert a number no larger than (days)"

    # run the tests
if __name__ == "__main__":
    unittest.main()



