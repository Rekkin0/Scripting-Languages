from retrieve_data import retrieve_data

from typing import List


def filter_download_time() -> List[str]:
    
    filtered_requests = []
    for line in retrieve_data().splitlines(True):
        
        try:
            download_datetime = line.split()[3].split("[")[1].split(":")
            download_hour = int(download_datetime[1])
            if download_hour >= 6 and download_hour < 22:
                filtered_requests.append(line)
        except:
            continue
        
    return filtered_requests


if __name__ == "__main__":
    
    print(*filter_download_time())