# aggregation
from pathlib import Path

from utils import LogDict, parse_log


def get_log_list(file_path: Path) -> list[str]:
    with open(file_path) as file:
        return file.readlines()


def get_log_dicts(file_path: Path) -> list[LogDict]:
    return [parse_log(log) for log in get_log_list(file_path)]
    
