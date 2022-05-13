import unittest
import os
import sys


# Change the path varialbe so we can get at the
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import python_utils_package.stringutils as su


class Test_StringBuilder(unittest.TestCase):
    """
    StringBuilder tests
    """
    def test_initializer(self):
        """
        Test the initalizer
        """
        test_string = "First, "

        sb = su.StringBuilder(test_string)
        actual = sb.tostring()
        expected = test_string
        self.assertEqual(actual, expected, "Test test_ctor")

    def test_append(self):
        """
        Test the append method
        """
        test_string = "First, "
        test_string2 = "Second, "
        test_string3 = test_string + test_string2

        sb = su.StringBuilder(test_string)
        sb.append(test_string2)
        actual = sb.tostring()
        expected = test_string3
        self.assertEqual(actual, expected, "Test test_append")

    def test_append_nested(self):
        """
        Test the append method
        """
        test_string = "First, "
        test_string2 = "Second, "
        test_string3 = "Third"

        test_string4 = test_string + test_string2 + test_string3

        sb = su.StringBuilder(test_string)
        sb.append(test_string2).append(test_string3)
        actual = sb.tostring()
        expected = test_string4
        self.assertEqual(actual, expected, "Test test_append_nested")


if(__name__ == '__main__'):
    unittest.main()