from utils import Data, get_data, get_host


def filter_download_location(data: Data) -> list[str]:
    return [line.group() for line in data if get_host(line).endswith('.pl')]


if __name__ == '__main__':
    print(*filter_download_location(get_data()), sep='\n')