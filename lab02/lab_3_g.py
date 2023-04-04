from utils import Data, get_data, get_datetime


def filter_download_date(data: Data) -> list[str]:
    return [line.group() for line in data if get_datetime(line).weekday() == 4]


if __name__ == '__main__':
    print(*filter_download_date(get_data()), sep='\n')