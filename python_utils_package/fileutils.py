"""
Python file utilities
"""

import pathlib


def getcurrentscriptdirectory() -> str:
    """
    Get the current script directory
    Return: directory of this script
    """
    script_dir = pathlib.Path(__file__).parent.resolve()
    return script_dir


def getcurrentworkingdirectory() -> str:
    """
    Get the current working directory
    Return: current working dir as string
    """
    cwd = pathlib.Path().resolve()
    return cwd