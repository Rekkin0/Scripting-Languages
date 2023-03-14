from retrieve_data import retrieve_data


def reduce_resource_size() -> float:
    
    total_resource_size = 0
    for line in retrieve_data().splitlines(True):
        
        try:
            resource_size = line.split()[9]
            if resource_size == "-":
                continue
            total_resource_size += int(resource_size)
        except:
            continue

    return total_resource_size


if __name__ == "__main__":
    
    resource_size_in_gb = reduce_resource_size() / (1000 ** 3)
    print(f"{round(resource_size_in_gb, 2)} GB")