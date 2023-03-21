from retrieve_data import retrieve_data

from typing import List


def reduce_resource_size(data: List[str]) -> float:
    
    total_resource_size = 0
    for line in data:
        
        try:
            resource_size = line.split()[9]
            if resource_size == "-":
                continue
            total_resource_size += int(resource_size)
        except:
            continue

    return round(total_resource_size / (1000 ** 3), 2)


if __name__ == "__main__":
    
    data = retrieve_data().splitlines(True)
    print(f"{reduce_resource_size(data)} GB")