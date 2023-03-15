from retrieve_data import retrieve_data

from typing import List


def filter_download_location() -> List[str]:
    
    filtered_requests = []
    data = retrieve_data().splitlines(True)
    for line in data:
        
        try:
            download_location = line.split()[0]
            if download_location.endswith(".pl"):
                filtered_requests.append(line)
        except:
            continue

    return filtered_requests


if __name__ == "__main__":
    
    print(*filter_download_location())