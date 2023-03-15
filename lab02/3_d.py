from retrieve_data import retrieve_data


def reduce_image_ratio() -> float:
    
    total_resource_count = 0
    image_count = 0
    image_formats = (".gif", ".jpg", ".jpeg", ".xbm")
    data = retrieve_data().splitlines(True)
    for line in data:
        
        try:
            if line.split()[6].endswith(image_formats):
                image_count += 1
            total_resource_count += 1
        except:
            continue
            
    return round(image_count / total_resource_count, 2)


if __name__ == "__main__":
    
    print(reduce_image_ratio())