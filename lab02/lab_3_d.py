from utils import retrieve_data, process_data, get_resource_path
from typing import List, Match


def reduce_image_ratio(data: List[Match[str]]) -> float:
    image_count = 0
    image_extensions = (".gif", ".jpg", ".jpeg", ".xbm")
    other_resource_count = 0
    for line in data:
        try:
            if get_resource_path(line).endswith(image_extensions):
                image_count += 1
            else:
                other_resource_count += 1
        except:
            continue
            
    return round(image_count / other_resource_count, 2)


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(reduce_image_ratio(data))