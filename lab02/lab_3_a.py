from retrieve_data import retrieve_data

from typing import List


def reduce_request(data: List[str], request_code: str) -> int:
    
    request_count = 0
    for line in data:
        
        try:
            curr_request_code = line.split()[8]
            if curr_request_code == request_code:
                request_count += 1
        except:
            continue
    
    return request_count