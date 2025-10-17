import unittest
from compIntCalc import *

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if results correct
    def test_days(self):
        self.assertEqual(total_amount_saved = comp_in_calc(800, 0.05, 24), 882.0)

        #user input only be between min_number_week_days and max_number_week_days


# make sure user cant input value greater than 7 for days

#i wanna add a try thingy so maybe a self.assert(equal) to an error message of "Insert a number no larger than (days)"

    # run the tests
if __name__ == "__main__":
    unittest.main()