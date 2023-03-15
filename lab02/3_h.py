from retrieve_data import retrieve_data

from typing import List


def filter_download_location() -> List[str]:
    
    filtered_download_locations = []
    data = retrieve_data().splitlines(True)
    for line in data:
        
        try:
            download_location = line.split()[0]
            if download_location.endswith(".pl"):
                filtered_download_locations.append(line)
        except:
            continue

    return filtered_download_locations


if __name__ == "__main__":
    
    print(*filter_download_location())