from typing import List, Tuple
from datetime import datetime


def get_datetime(datetime_raw: str) -> datetime:
    # przetwarzanie daty
    date_raw = datetime_raw.split(':')[0].split('/')
    year     = int(date_raw[2])
    month    = datetime.strptime(date_raw[1], "%b").month
    day      = int(date_raw[0])
    
    # przetwarzanie czasu
    time_raw = datetime_raw.split(':')
    hour     = int(time_raw[1])
    minute   = int(time_raw[2])
    second   = int(time_raw[3])
    
    return datetime(year, month, day, hour, minute, second)


def read_log() -> List[Tuple]:
    
    log = []
    
    while True:
        try:
            line = input().split()
            
            host          = line[0]
            datetime      = get_datetime(line[3].strip('['))
            http_method   = line[5].strip('"')
            resource_path = line[6]
            http_version  = line[7].strip('"')
            http_code     = int(line[8])
            if line[9] == '-':
                resource_size = 0
            else:
                resource_size = int(line[9])
            
            log.append((host, datetime, http_method, resource_path, http_version, http_code, resource_size))
        except EOFError:
            break
        except:
            continue
        
    return log


def sort_log(log: List[Tuple], sort_by: int) -> List[Tuple]:
    try:
        sorted_log = sorted(log, key = lambda tuple: tuple[sort_by])
        return sorted_log    
    except IndexError:
        print("Failed to sort log. Invalid index of element to sort by.")
        return log
    except:
        print("Failed to sort log. Unknown error.")
        return log
    
    
def get_entries_by_addr(log: List[Tuple], address: str) -> List[Tuple]:
    
    return [entry for entry in log if entry[0] == address]


def get_entries_by_code(log: List[Tuple], code: int) -> List[Tuple]:
    
    if type(code) is not int or not 100 <= code < 600:
        print("Failed to get entries by code. Invalid code.")
        return [] 
    
    return [entry for entry in log if entry[5] == code]
    
    
def get_failed_reads(log: List[Tuple], join_entries: bool = False) -> List[Tuple] | Tuple[List[Tuple], List[Tuple]]:
    
    entries_4xx = [entry for entry in log if entry[5] // 100 == 4]
    entries_5xx = [entry for entry in log if entry[5] // 100 == 5]
    
    if join_entries:
        return entries_4xx + entries_5xx
    return entries_4xx, entries_5xx
    
    
def get_entries_by_extension(log: List[Tuple], extension: str) -> List[Tuple]:
    
    return [entry for entry in log if entry[3].endswith(extension)]


def print_entries(log: List[Tuple]) -> None:
    
    print(*log, sep = '\n')\
