import re
from typing import Any

from utils import LogDict


# ZAD 2a w pliku utils.py

IPV4_REGEX = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')   

def get_ipv4s_from_log(log: LogDict) -> list[Any]:
    message = log['message']
    assert isinstance(message, str)
    
    return IPV4_REGEX.findall(message)


USER_REGEX = re.compile(r'\buser(?: +|=)(?!authentication\b)(?P<user>\w+)')
ACCEPTED_USER_REGEX = re.compile(r'Accepted password for (?P<user>\w+)')

def get_user_from_log(log: LogDict) -> str | None:
    message = log['message']
    assert isinstance(message, str)
    match = USER_REGEX.search(message)
    if match is None:
        match = ACCEPTED_USER_REGEX.search(message)
        
    return match.group('user') if match is not None else None


LOGIN_SUCCESS_REGEX = re.compile(r'Accepted password')
LOGIN_FAILURE_REGEX = re.compile(r'authentication failure')
CONNECTION_CLOSED_REGEX = re.compile(r'Connection closed|Received disconnect')
INVALID_PASSWORD_REGEX = re.compile(r'Failed password')
INVALID_USER_REGEX = re.compile(r'Invalid user')
BREAK_IN_ATTEMPT_REGEX = re.compile(r'POSSIBLE BREAK-IN ATTEMPT!')
MESSAGE_TYPES = {
    LOGIN_SUCCESS_REGEX    : 'login success',
    LOGIN_FAILURE_REGEX    : 'login failure',
    CONNECTION_CLOSED_REGEX: 'connection closed',
    INVALID_PASSWORD_REGEX : 'invalid password',
    INVALID_USER_REGEX     : 'invalid user',
    BREAK_IN_ATTEMPT_REGEX : 'break-in attempt'
}

def get_message_type(message: str) -> str:
    for regex, message_type in MESSAGE_TYPES.items():
        if regex.search(message):
            return message_type
    return 'other'