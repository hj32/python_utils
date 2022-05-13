import unittest
import os
import sys
import pathlib


# Change the path varialbe so we can get at the
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import python_utils_package.fileutils as fu


class Test_Object(unittest.TestCase):
    def test_getcurrentscriptdirectory(self):
        """
        Test getcurrentscriptdirectory
        """
        script_dir = fu.getcurrentscriptdirectory()

        path_obj = pathlib.Path(script_dir)

        self.assertTrue(path_obj.exists, "Test getcurrentscripdirectory")

    def test_getcurrentworkingdirectory(self):
        """
        Test get currentworkingdirectory
        """
        cwd = fu.getcurrentworkingdirectory()

        path_obj = pathlib.Path(cwd)

        self.assertTrue(path_obj.exists, "Test getcurrentworkingdirectory")


if(__name__ == '__main__'):
    unittest.main()