from datetime import datetime

from list_tuple_practice import Entry, Log


DictEntry = dict[str, str | datetime | int]
LogDict = dict[str, list[DictEntry]]


def entry_to_dict(entry: Entry) -> DictEntry:
    keys = ('host', 'timestamp', 'resource_path', 'status_code', 'resource_size')
    return dict(zip(keys, entry))


def log_to_dict(log: Log) -> LogDict:
    log_dict = {}
    for entry in log:
        host = entry[0]
        if host not in log_dict:
            log_dict[host] = []
        log_dict[host].append(entry_to_dict(entry))
        
    return log_dict


def get_addrs(log_dict: LogDict) -> list[str]:
    return list(log_dict.keys())


def print_dict_entry_dates(log_dict: LogDict) -> None:
    for host, entries in log_dict.items():
        first_request_date  = entries[0]['timestamp']
        last_request_date   = entries[-1]['timestamp']
        total_request_count = len(entries)
        successful_request_count = sum(1 for entry in entries if entry['status_code'] == 200)
        successful_request_ratio = round(successful_request_count / total_request_count, ndigits=2)
        
        print(f"{host:<53}\t{total_request_count}\t{first_request_date}\t{last_request_date}\t{successful_request_ratio}")
