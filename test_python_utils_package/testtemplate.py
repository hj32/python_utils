import unittest
import os
import sys


# Change the path varialbe so we can get at the
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


class Test_Object(unittest.TestCase):
    def test_method(self):

        actual = 0
        expected = 0
        self.assertEqual(actual, expected, "Check test_method")


if(__name__ == '__main__'):
    unittest.main()