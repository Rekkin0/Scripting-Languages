# parsing
import re
from datetime import datetime
from typing import Any


LogDict = dict[str, Any]


LOG_REGEX = re.compile(r'(\w{3} {1,2}\d{1,2} \d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')
TIMESTAMP_FORMAT = '%Y %b %d %H:%M:%S'

def parse_log(line: str) -> LogDict:
    """
    Parse a log line to a dictionary.
    """
    match = LOG_REGEX.match(line)
    if match is None:
        raise Exception(f'Invalid line: {line}')
        
    timestamp, hostname, process, message = match.groups()
    
    return {
        'bytes'    : len(line),
        'timestamp': datetime.strptime('2023 ' + timestamp, TIMESTAMP_FORMAT),
        'hostname' : hostname,
        'process'  : int(process),
        'message'  : message
    }


IPV4_REGEX = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')   

def get_ipv4s_from_log(log: LogDict) -> list[Any]:
    """
    Return a list of IPv4 addresses in a log line.
    """
    assert isinstance(message := log['message'], str)
    
    return IPV4_REGEX.findall(message)


USER_REGEX = re.compile(r'\buser(?: +|=)(?!authentication\b)(?P<user>\w+)')
ACCEPTED_USER_REGEX = re.compile(r'Accepted password for (?P<user>\w+)')

def get_user_from_log(log: LogDict) -> str | None:
    """
    Return the user in a log line.
    """
    assert isinstance(message := log['message'], str)
    match = USER_REGEX.search(message)
    if match is None:
        match = ACCEPTED_USER_REGEX.search(message)
        
    return match.group('user') if match is not None else None


LOGIN_SUCCESS_TYPENAME,     LOGIN_SUCCESS_REGEX     = 'login success',     re.compile(r'Accepted password')
LOGIN_FAILURE_TYPENAME,     LOGIN_FAILURE_REGEX     = 'login failure',     re.compile(r'authentication failure')
CONNECTION_CLOSED_TYPENAME, CONNECTION_CLOSED_REGEX = 'connection closed', re.compile(r'Connection closed|Received disconnect')
INVALID_PASSWORD_TYPENAME,  INVALID_PASSWORD_REGEX  = 'invalid password',  re.compile(r'Failed password')
INVALID_USER_TYPENAME,      INVALID_USER_REGEX      = 'invalid user',      re.compile(r'Invalid user', re.IGNORECASE)
BREAK_IN_ATTEMPT_TYPENAME,  BREAK_IN_ATTEMPT_REGEX  = 'break-in attempt',  re.compile(r'POSSIBLE BREAK-IN ATTEMPT!')

TYPENAMES = (LOGIN_SUCCESS_TYPENAME, LOGIN_FAILURE_TYPENAME, CONNECTION_CLOSED_TYPENAME, 
             INVALID_PASSWORD_TYPENAME, INVALID_USER_TYPENAME, BREAK_IN_ATTEMPT_TYPENAME)
REGEXES   = (LOGIN_SUCCESS_REGEX, LOGIN_FAILURE_REGEX, CONNECTION_CLOSED_REGEX, 
             INVALID_PASSWORD_REGEX, INVALID_USER_REGEX, BREAK_IN_ATTEMPT_REGEX)
MESSAGE_TYPES = dict(zip(TYPENAMES, REGEXES))

OTHER_TYPENAME = 'other'

def get_message_type(message: str) -> str:
    """
    Return the type of a message.
    """
    for message_type, regex in MESSAGE_TYPES.items():
        if regex.search(message):
            return message_type
    return OTHER_TYPENAME
