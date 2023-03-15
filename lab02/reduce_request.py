from retrieve_data import retrieve_data


def reduce_request(request_code: str) -> int:
    
    request_count = 0
    data = retrieve_data().splitlines(True)
    for line in data:
        
        try:
            curr_request_code = line.split()[8]
            if curr_request_code == request_code:
                request_count += 1
        except:
            continue
    
    return request_count