"""
String Utils
"""
import string
from io import StringIO


class StringBuilder:
    """
    StringBuilder class
    """
    _file_str = None

    def __init__(self, str=""):
        """
        Initializer for StringBuilder
        str: string to append to StringBuilder
        """
        self._file_str = StringIO()
        self._file_str.write(str)

    def append(self, str=""):
        """
        Append string to the StringBuilder
        str: string to append to StringBuilder
        returns: self so you can nest calls to append
        """
        self._file_str.write(str)
        return self

    def tostring(self):
        """
        Convert the StringBuilder to a string
        Return: string representing the content of the StringBuilder
        """
        return self._file_str.getvalue()