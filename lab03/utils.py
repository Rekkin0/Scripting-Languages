import re
from typing import Match
from datetime import datetime


def retrieve_raw_data() -> str:
    data = ''
    while True:
        try:
            data += input() + '\n'
        except EOFError:
            break
        
    return data


REGEX = re.compile(r'(.+) - - \[(.+)\] \"(.+)\" (.+) (.+)')

def process_raw_line(raw_line: str) -> Match[str]:
    line = REGEX.match(raw_line)
    if line is None:
        raise Exception(f'Invalid line: {raw_line}')
    
    return line


def process_raw_data(raw_data: list[str]) -> list[Match[str]]:
    data = []
    for line in raw_data:
        try:
            data.append(process_raw_line(line))
        except Exception as e:
            # print(e)
            continue
    
    return data


def get_data() -> list[Match[str]]:
    raw_data = retrieve_raw_data().splitlines(True)
    data = process_raw_data(raw_data)
    
    return data


def get_host(line: Match[str]) -> str:
    return line.group(1)


def get_datetime(line: Match[str]) -> datetime:
    timestamp = line.group(2).split()[0]
    
    return datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S')


def get_request(line: Match[str]) -> str:
    return line.group(3)


def get_resource_path(line: Match[str]) -> str:
    request = get_request(line).split()
    
    return (request[1] if len(request) > 1 else request[0]).strip()
    

def get_status_code(line: Match[str]) -> int:
    try:
        return int(line.group(4))
    except:
        return 0


def get_resource_size(line: Match[str]) -> int:
    try:
        return int(line.group(5))
    except:
        return 0
