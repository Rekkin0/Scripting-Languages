from retrieve_data import retrieve_data

from typing import List


def filter_download_time(data: List[str]) -> List[str]:
    
    filtered_download_times = []
    for line in data:
        
        try:
            download_datetime = line.split()[3].split("[")[1].split(":")
            download_hour = int(download_datetime[1])
            if download_hour >= 22 or download_hour < 6:
                filtered_download_times.append(line)
        except:
            continue
        
    return filtered_download_times


if __name__ == "__main__":
    
    data = retrieve_data().splitlines(True)
    print(*filter_download_time(data))