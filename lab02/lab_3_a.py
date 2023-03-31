from utils import get_status_code
from typing import Match


def reduce_request(data: list[Match[str]], status_code: int) -> int:
    return sum(1 for line in data if get_status_code(line) == status_code)