from utils import *


Entry = tuple[str, datetime, str, int, int]
Log = list[Entry]


def read_log() -> Log:
    log = []
    for line in get_data():
        host          = get_host(line)
        timestamp     = get_datetime(line)
        resource_path = get_resource_path(line)
        status_code   = get_status_code(line)
        resource_size = get_resource_size(line)
        log.append((host, timestamp, resource_path, status_code, resource_size))
        
    return log


def sort_log(log: Log, sort_by: int) -> Log:
    try: 
        return sorted(log, key = lambda tuple: tuple[sort_by])   
    except IndexError: 
        print('Failed to sort log. Invalid index of element to sort by.')
    except: 
        print('Failed to sort log. Unknown error.')
    return log
    
    
def get_entries_by_addr(log: Log, address: str) -> Log:
    return [entry for entry in log if entry[0] == address]


def get_entries_by_code(log: Log, code: int) -> Log:
    if not 100 <= code < 600:
        print('Failed to get entries by code. Invalid code.')
        return [] 
    
    return [entry for entry in log if entry[3] == code]
    
    
def get_failed_reads(log: Log, join_entries: bool = False) -> Log | tuple[Log, Log]:
    entries_4xx = [entry for entry in log if entry[3] // 100 == 4]
    entries_5xx = [entry for entry in log if entry[3] // 100 == 5]
    
    return entries_4xx + entries_5xx if join_entries else entries_4xx, entries_5xx

    
def get_entries_by_extension(log: Log, extension: str) -> Log:
    return [entry for entry in log if entry[2].endswith(extension)]


def print_entries(log: Log) -> None:
    print(*log, sep = '\n')
