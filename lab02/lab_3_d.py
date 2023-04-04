from utils import Data, get_data, get_resource_path


def reduce_image_ratio(data: Data) -> float:
    image_extensions = ('.gif', '.jpg', '.jpeg', '.xbm')
    image_count = sum(1 for line in data if get_resource_path(line).endswith(image_extensions))
    other_resource_count = len(data) - image_count
        
    return round(image_count / other_resource_count, ndigits=2)


if __name__ == '__main__':
    print(reduce_image_ratio(get_data()))