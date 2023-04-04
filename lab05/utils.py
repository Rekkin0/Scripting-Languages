import re
import datetime


LogDict = dict[str, datetime.date | datetime.time | str]


LOG_REGEX = re.compile(r'(\w{3} \d{1,2}) (\d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')

def parse_log(log: str) -> LogDict:
    match = LOG_REGEX.match(log)
    if match is None:
        raise Exception(f'Invalid line: {log}')
    date, time, host, process, message = match.groups()
    
    return {
        'date': datetime.datetime.strptime(date, '%b %d').date(),
        'time': datetime.datetime.strptime(time, '%H:%M:%S').time(),
        'host': host, 
        'process': process, 
        'message': message
    }