import re
from datetime import datetime
from pathlib import Path


LogDict = dict[str, datetime | int | str]

LOG_PATH = Path(__file__).parent / 'SSH.log'
LOG_REGEX = re.compile(r'(\w{3} {1,2}\d{1,2}) (\d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')

def parse_log(line: str) -> LogDict:
    match = LOG_REGEX.match(line)
    if match is None:
        print(f'Invalid line: {line}')
        exit()
    date, time, host, process, message = match.groups()
    
    return {
        'bytes'  : len(line),
        'date'   : datetime.strptime(date, '%b %d'),
        'time'   : datetime.strptime(time, '%H:%M:%S'),
        'host'   : host, 
        'process': process, 
        'message': message
    }