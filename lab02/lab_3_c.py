from utils import retrieve_data, process_data, get_resource_size, get_resource_path
from typing import List, Tuple, Match


def reduce_largest_resource(data: List[Match[str]]) -> Tuple[str, int]:
  
    largest_resource_path = ""    
    largest_resource_size = 0
    for line in data:
        try:
            resource_path, resource_size = get_resource_path(line), int(get_resource_size(line))
            if resource_size > largest_resource_size:
                largest_resource_path, largest_resource_size = resource_path, resource_size
        except:
            continue
            
    return largest_resource_path, largest_resource_size


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(reduce_largest_resource(data))