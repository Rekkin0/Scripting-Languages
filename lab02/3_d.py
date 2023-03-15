from retrieve_data import retrieve_data


def reduce_image_ratio() -> float:
    
    total_resource_count = 0
    image_count = 0
    image_formats = (".gif", ".jpg", ".jpeg", ".xbm")
    for line in retrieve_data().splitlines(True):
        
        try:
            if line.split()[6].endswith(image_formats):
                image_count += 1
            total_resource_count += 1
        except:
            continue
            
    return round(image_count / total_resource_count, 2)


if __name__ == "__main__":
    
    print(reduce_image_ratio())