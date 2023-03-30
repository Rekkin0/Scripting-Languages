from utils import retrieve_data, process_data, get_timestamp
from typing import List, Match
from datetime import datetime


def filter_download_time(data: List[Match[str]]) -> List[str]:
    filtered_download_times = []
    for line in data:
        try:
            timestamp = get_timestamp(line)
            date_time = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")
            if date_time.hour >= 22 or date_time.hour < 6:
                filtered_download_times.append(line)
        except:
            continue
        
    return filtered_download_times


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(*filter_download_time(data))