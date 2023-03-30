from utils import retrieve_data, process_data, get_resource_size
from typing import List, Match


def reduce_resource_size(data: List[Match[str]]) -> float:
    total_resource_size = 0
    for line in data:
        try:
            total_resource_size += int(get_resource_size(line))
        except:
            continue

    return round(total_resource_size / (1000 ** 3), 2)


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data) 
    print(f"{reduce_resource_size(data)} GB")