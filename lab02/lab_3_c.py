from utils import Data, get_data, get_resource_size, get_resource_path


def reduce_largest_resource(data: Data) -> tuple[str, int]:
    largest_resource = max(data, key=lambda line: get_resource_size(line))
    largest_resource_path = get_resource_path(largest_resource)
    largest_resource_size = get_resource_size(largest_resource)
        
    return largest_resource_path, largest_resource_size


if __name__ == '__main__':
    print(reduce_largest_resource(get_data()))