import unittest
from unittest import mock
from unittest.mock import Mock, MagicMock, patch
import unittest.mock as mock
from compIntCalc import comp_in_calc

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if results correct
    def test_days(self):
        self.assertEqual(comp_in_calc(800, 0.05, 24), 882.0)

        #user input only be between min_number_week_days and max_number_week_days


# make sure user cant input value greater than 7 for days

#i wanna add a try thingy so maybe a self.assert(equal) to an error message of "Insert a number no larger than (days)"

    # run the tests
if __name__ == "__main__":
    unittest.main()