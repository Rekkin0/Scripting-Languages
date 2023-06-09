# logging
import logging, sys
from datetime import datetime

from exc1 import get_log_dicts
from exc2 import LOGIN_SUCCESS_TYPENAME, LOGIN_FAILURE_TYPENAME, CONNECTION_CLOSED_TYPENAME, \
                 INVALID_PASSWORD_TYPENAME, INVALID_USER_TYPENAME, BREAK_IN_ATTEMPT_TYPENAME, \
                 OTHER_TYPENAME, LogDict, get_message_type


logging.basicConfig(level=logging.INFO, format='— %(levelname)-8s — %(message)s')
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

LEVEL_TEXT_TO_LOG_LEVEL = {
    'debug'   : logging.DEBUG,
    'info'    : logging.INFO,
    'warning' : logging.WARNING,
    'error'   : logging.ERROR,
    'critical': logging.CRITICAL,
}


def set_logging_level(level: str) -> None:
    """
    Set the logging level.
    """
    logger.setLevel(LEVEL_TEXT_TO_LOG_LEVEL[level])


def log_timestamp(timestamp: datetime) -> None:
    """
    Log a timestamp given date and time.
    """
    date, time = timestamp.date(), timestamp.time()
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
        log_timestamp(log['timestamp']) # type: ignore
    logger.log(log_level, message)
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        set_logging_level(sys.argv[1])
    [log_entry(log) for log in get_log_dicts('SSH.log')]
