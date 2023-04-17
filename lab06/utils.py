import re
from datetime import datetime
from typing import Any


LogDict = dict[str, datetime | int | str]

LOG_REGEX  = re.compile(r'(\w{3} {1,2}\d{1,2} \d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')
IPV4_REGEX = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
TIMESTAMP_FORMAT = '%b %d %H:%M:%S'  


def parse_log(line: str) -> LogDict:
    """
    Parse a log line to a dictionary.
    """
    match = LOG_REGEX.match(line)
    if match is None:
        raise SystemExit(f'Invalid line: {line}')
    timestamp, hostname, process, message = match.groups()
    
    return {
        'bytes'    : len(line),
        'timestamp': datetime.strptime(timestamp, TIMESTAMP_FORMAT),
        'hostname' : hostname,
        'process'  : int(process),
        'message'  : message
    }


def get_ipv4s_from_log(log: LogDict) -> list[Any]:
    """
    Return a list of IPv4 addresses in a log line.
    """
    assert isinstance(message := log['message'], str)
    
    return IPV4_REGEX.findall(message)