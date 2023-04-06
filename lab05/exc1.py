# aggregation
from pathlib import Path

from utils import LogDict, parse_log


def get_lines(file_path: Path) -> list[str]:
    """
    Return a list of lines in a file.
    """
    with open(file_path) as file:
        return file.readlines()


def get_log_dicts(file_path: Path) -> list[LogDict]:
    """
    Return a list of log dictionaries in a file.
    """
    return [parse_log(line) for line in get_lines(file_path)]
    
