from utils import retrieve_data, process_data, get_host
from typing import List, Match


def filter_download_location(data: List[Match[str]]) -> List[str]:
    filtered_download_locations = []
    for line in data:
        try:
            host = get_host(line)
            if host.endswith(".pl"):
                filtered_download_locations.append(line)
        except:
            continue

    return filtered_download_locations


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(*filter_download_location(data))