from utils import get_status_code
from typing import List, Match


def reduce_request(data: List[Match[str]], status_code: str) -> int:
    request_count = 0
    for line in data:
        try:
            curr_status_code = get_status_code(line)
            if curr_status_code == status_code:
                request_count += 1
        except:
            continue
    
    return request_count