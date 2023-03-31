from utils import get_data, get_host
from typing import Match


def filter_download_location(data: list[Match[str]]) -> list[str]:
    return [line.group() for line in data if get_host(line).endswith('.pl')]


if __name__ == '__main__':
    print(*filter_download_location(get_data()), sep='\n')