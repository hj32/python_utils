"""
Python file utilities
"""
import string
import pathlib


def getcurrentscriptdirectory():
    """
    Get the current script directory
    Return: directory of this script
    """
    script_dir = pathlib.Path(__file__).parent.resolve()
    return script_dir


def getcurrentworkingdirectory() -> string:
    """
    Get the current working directory
    Return: current working dir as string
    """
    cwd = pathlib.Path().resolve()
    return cwd