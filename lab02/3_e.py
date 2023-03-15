from retrieve_data import retrieve_data

from typing import List


def filter_requests() -> List[str]:
    
    filtered_requests = []
    data = retrieve_data().splitlines(True)
    for line in data:
        
        try:
            request_code = line.split()[8]
            if request_code == "200":
                filtered_requests.append(line)
        except:
            continue
        
    return filtered_requests


if __name__ == "__main__":
    
    print(*filter_requests())