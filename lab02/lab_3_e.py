from utils import retrieve_data, process_data, get_status_code
from typing import List, Match


def filter_requests(data: List[Match[str]]) -> List[str]:
    filtered_requests = []
    for line in data:
        try:
            if get_status_code(line) == "200":
                filtered_requests.append(line)
        except:
            continue
        
    return filtered_requests


if __name__ == "__main__":
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(*filter_requests(data))