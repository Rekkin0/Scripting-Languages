# logging
import logging, sys
from datetime import datetime
from typing import Any

from exc01 import get_log_list
from exc02 import LOGIN_SUCCESS_TYPENAME, LOGIN_FAILURE_TYPENAME, CONNECTION_CLOSED_TYPENAME, \
                  INVALID_PASSWORD_TYPENAME, INVALID_USER_TYPENAME, BREAK_IN_ATTEMPT_TYPENAME, \
                  OTHER_TYPENAME, get_message_type
from utils import LogDict, LOG_PATH, parse_log


log_format = logging.Formatter('— %(levelname)-8s — %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

debug_handler = logging.StreamHandler(sys.stdout)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(log_format)
debug_handler.addFilter(lambda record: record.levelno == logging.DEBUG)
logger.addHandler(debug_handler)

info_handler = logging.StreamHandler(sys.stdout)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(log_format)
info_handler.addFilter(lambda record: record.levelno == logging.INFO)
logger.addHandler(info_handler)

warning_handler = logging.StreamHandler(sys.stdout)
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(log_format)
warning_handler.addFilter(lambda record: record.levelno == logging.WARNING)
logger.addHandler(warning_handler)

error_handler = logging.StreamHandler(sys.stderr)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(log_format)
error_handler.addFilter(lambda record: record.levelno == logging.ERROR)
logger.addHandler(error_handler)

critical_handler = logging.StreamHandler(sys.stderr)
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(log_format)
critical_handler.addFilter(lambda record: record.levelno == logging.CRITICAL)
logger.addHandler(critical_handler)

def log_by_level(level: int, date: datetime, time: datetime, message: str) -> None:
    if logger.getEffectiveLevel() > level:
        return
    print_timestamp(date, time)
    
    

MESSAGE_TYPE_TO_LOG = {
    LOGIN_SUCCESS_TYPENAME    : logging.INFO,
    CONNECTION_CLOSED_TYPENAME: logging.INFO,
    LOGIN_FAILURE_TYPENAME    : logging.WARNING,
    INVALID_PASSWORD_TYPENAME : logging.ERROR,
    INVALID_USER_TYPENAME     : logging.ERROR,
    BREAK_IN_ATTEMPT_TYPENAME : logging.CRITICAL,
    OTHER_TYPENAME            : logging.DEBUG,
}


def log_read_bytes(raw_log: Any) -> None:
    logger.debug(f'Read {len(raw_log)} bytes')


def print_timestamp(date: datetime, time: datetime) -> None:
    assert isinstance(date, datetime)
    print(date.strftime('%b %d').replace(' 0', '  '), end=' ')
    assert isinstance(time, datetime)
    print(time.strftime('%H:%M:%S'), end=' ', flush=True)


def log_line(raw_log: Any) -> None:
    log = parse_log(raw_log)
    log_read_bytes(raw_log)
    assert isinstance(date := log['date'], datetime)
    assert isinstance(time := log['time'], datetime)
    assert isinstance(message := log['message'], str)
    message_type = get_message_type(message)
    if message_type in MESSAGE_TYPE_TO_LOG:
        level = MESSAGE_TYPE_TO_LOG[message_type]
        log_by_level(level, date, time, message)
        

if __name__ == '__main__':
    for i, log in enumerate(get_log_list(LOG_PATH)):
        log_line(log)
        if i == 10:
            break
        
    # [log_line(log) for log in get_log_list(LOG_PATH)]
