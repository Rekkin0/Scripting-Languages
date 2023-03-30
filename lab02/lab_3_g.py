from utils import retrieve_data, process_data, get_timestamp
from typing import List, Match
from datetime import datetime


def filter_download_date(data: List[Match[str]]) -> List[str]:
    filtered_download_dates = []
    for line in data:
        try:
            timestamp = get_timestamp(line)
            date_time = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")
            if date_time.weekday == 4:
                filtered_download_dates.append(line)
        except:
            continue
        
    return filtered_download_dates


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(*filter_download_date(data))