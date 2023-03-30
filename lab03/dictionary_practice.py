from typing import List, Tuple, Dict, Any


def entry_to_dict(entry: Tuple) -> Dict[str, Any]:
    
    keys = ('host', 'datetime', 'http_method', 'resource_path', 'http_version', 'http_code', 'resource_size')
    return dict(zip(keys, entry))


def log_to_dict(log: List[Tuple]) -> Dict[str, List[Dict[str, Any]]]:
    
    log_dict = {}
    for entry in log:
        host = entry[0]
        if host not in log_dict.keys():
            log_dict[host] = []
        log_dict[host].append(entry_to_dict(entry))
    
    return log_dict


def get_addrs(log_dict: Dict[str, List[Dict[str, Any]]]) -> List[str]:
    
    return [key for key in log_dict.keys()]


def print_dict_entry_dates(log_dict: Dict[str, List[Dict[str, Any]]]) -> None:
    
    for key, value in log_dict.items():
        host = key
        first_request_date    = value[0]['datetime']
        last_request_date     = value[-1]['datetime']
        total_request_count   = len(value)
        success_request_count = sum([1 for entry in value if entry['http_code'] == 200])
        success_request_ratio = round(success_request_count / total_request_count, 2)
        
        print(f"{host:<53}\t{total_request_count}\t{first_request_date}\t{last_request_date}\t{success_request_ratio}")
