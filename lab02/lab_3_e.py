from utils import get_data, get_status_code
from typing import Match


def filter_requests(data: list[Match[str]]) -> list[str]:
    return [line.group() for line in data if get_status_code(line) == 200]


if __name__ == '__main__':
    print(*filter_requests(get_data()), sep='\n')