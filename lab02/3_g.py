from retrieve_data import retrieve_data

from typing import List
from datetime import datetime


def filter_download_date() -> List[str]:
    
    filtered_requests = []
    data = retrieve_data().splitlines(True)
    for line in data:
        
        try:
            download_datetime = line.split()[3].split("[")[1].split(":")
            download_date = download_datetime[0].split("/")
            download_month_number = datetime.strptime(download_date[1], "%b").month
            download_day = datetime(int(download_date[2]), download_month_number, int(download_date[0])).strftime("%A")
            if download_day == "Friday":
                filtered_requests.append(line)
        except:
            continue
        
    return filtered_requests


if __name__ == "__main__":
    
    print(*filter_download_date())