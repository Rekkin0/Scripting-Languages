from utils import get_data, get_resource_size
from typing import Match


def reduce_resource_size(data: list[Match[str]]) -> float:
    total_resource_size = sum(get_resource_size(line) for line in data)

    return round(total_resource_size / (1000 ** 3), ndigits=2)


if __name__ == '__main__': 
    print(f"{reduce_resource_size(get_data())} GB")