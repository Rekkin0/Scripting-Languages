import re
from datetime import datetime
from pathlib import Path


LogDict = dict[str, datetime | int | str]

LOG_PATH = Path(__file__).parent / 'SSH.log'


LOG_REGEX = re.compile(r'(\w{3} {1,2}\d{1,2}) (\d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')

def parse_log(log: str) -> LogDict:
    match = LOG_REGEX.match(log)
    if match is None:
        raise Exception(f'Invalid line: {log}')
    date, time, host, process, message = match.groups()
    
    return {
        'date'   : datetime.strptime(date, '%b %d'),
        'time'   : datetime.strptime(time, '%H:%M:%S'),
        'host'   : host, 
        'process': process, 
        'message': message
    }