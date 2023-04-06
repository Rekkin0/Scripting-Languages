# logging
import logging, sys
from datetime import datetime

from exc1 import LogDict, get_log_dicts
from exc2 import LOGIN_SUCCESS_TYPENAME, LOGIN_FAILURE_TYPENAME, CONNECTION_CLOSED_TYPENAME, \
                 INVALID_PASSWORD_TYPENAME, INVALID_USER_TYPENAME, BREAK_IN_ATTEMPT_TYPENAME, \
                 OTHER_TYPENAME, get_message_type
from utils import LOG_PATH


DateTime = tuple[datetime, datetime]


try:
    DEFAULT_LOGGING_LEVEL = int(sys.argv[1])
except:
    DEFAULT_LOGGING_LEVEL = logging.INFO

logging.basicConfig(level=DEFAULT_LOGGING_LEVEL, format='— %(levelname)-8s — %(message)s')
logger = logging.getLogger()

MESSAGE_TYPE_TO_LOG_LEVEL = {
    LOGIN_SUCCESS_TYPENAME    : logging.INFO,
    CONNECTION_CLOSED_TYPENAME: logging.INFO,
    LOGIN_FAILURE_TYPENAME    : logging.WARNING,
    INVALID_PASSWORD_TYPENAME : logging.ERROR,
    INVALID_USER_TYPENAME     : logging.ERROR,
    BREAK_IN_ATTEMPT_TYPENAME : logging.CRITICAL,
    OTHER_TYPENAME            : logging.DEBUG,
}


def log_timestamp(date: datetime, time: datetime) -> None:
    """
    Log a timestamp given date and time.
    """
    print(date.strftime('%b %d').replace(' 0', '  '), end=' ')
    print(time.strftime('%H:%M:%S'), end=' ', flush=True)


def log_entry(log: LogDict) -> None:
    """
    Log an entry from the log file represented as a dictionary.
    """
    message_type = get_message_type(message := log['message']) # type: ignore
    log_level = MESSAGE_TYPE_TO_LOG_LEVEL[message_type]
    
    logger.debug(f"{log['bytes']} bytes read")
    if logger.getEffectiveLevel() <= log_level:
        log_timestamp(log['date'], log['time']) # type: ignore
    logger.log(log_level, message)
        

if __name__ == '__main__':
    [log_entry(log) for log in get_log_dicts(LOG_PATH)]








""" debug_handler = logging.StreamHandler(sys.stdout)
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
logger.addHandler(critical_handler) """
