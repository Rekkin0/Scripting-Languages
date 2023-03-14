from retrieve_data import retrieve_data


def reduce_request(request_code: str) -> int:
    
    request_count = 0
    for line in retrieve_data().splitlines(True):
        try:
            if line.split()[8] == request_code:
                request_count += 1
        except:
            continue
    
    return request_count