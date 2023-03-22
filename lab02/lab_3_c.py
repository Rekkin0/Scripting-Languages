from retrieve_data import retrieve_data

from typing import List, Tuple


def reduce_largest_resource(data: List[str]) -> Tuple[str, int]:
  
    largest_resource_path = ""    
    largest_resource_size = 0
    for line in data:
        
        try:
            resource_path, resource_size = line.split()[6], line.split()[9]
            if resource_size == "-":
                continue
            if (resource_size := int(resource_size)) > largest_resource_size:
                largest_resource_path = resource_path
                largest_resource_size = resource_size
        except:
            continue
            
    return largest_resource_path, largest_resource_size


if __name__ == "__main__":
    
    data = retrieve_data().splitlines(True)
    print(reduce_largest_resource(data))