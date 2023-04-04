from utils import Data, get_data, get_datetime


def filter_download_time(data: Data) -> list[str]:
    return [line.group() for line in data if (hour := get_datetime(line).hour) >= 22 or hour < 6]


if __name__ == '__main__':
    print(*filter_download_time(get_data()), sep='\n')