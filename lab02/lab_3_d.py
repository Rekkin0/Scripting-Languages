from retrieve_data import retrieve_data

from typing import List


def reduce_image_ratio(data: List[str]) -> float:
    
    image_count = 0
    image_formats = (".gif", ".jpg", ".jpeg", ".xbm")
    other_resource_count = 0
    for line in data:
        
        try:
            if line.split()[6].endswith(image_formats):
                image_count += 1
            else:
                other_resource_count += 1
        except:
            continue
            
    return round(image_count / other_resource_count, 2)


if __name__ == "__main__":
    
    data = retrieve_data().splitlines(True)
    print(reduce_image_ratio(data))