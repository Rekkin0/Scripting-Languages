import re, statistics
from datetime import datetime
from collections import defaultdict

from exc1 import get_log_dicts
from exc2 import LogDict, get_user_from_log


SESSION_OPENED_REGEX = re.compile(r'session opened')
SESSION_CLOSED_REGEX = re.compile(r'session closed')

def get_session_end_log(logs: list[LogDict], process: int) -> LogDict | None:
    """
    Return the log of the end of an SSH session.
    """
    for log in logs:
        if (log['process'] == process and 
            SESSION_CLOSED_REGEX.search(log['message'])): # type: ignore
            return log
        

def get_session_duration(log_index: int, log: LogDict, logs: list[LogDict]) -> float | None:
    """
    Return the duration of an SSH session in seconds.
    """
    assert isinstance(message := log['message'], str)
    # check if the log is the start of an SSH session
    if SESSION_OPENED_REGEX.search(message) is None:
        return None
    
    assert isinstance(process := log['process'], int)
    session_end_log = get_session_end_log(logs[log_index:], process)
    
    if session_end_log is None:
        return None
    
    assert isinstance(session_start_time := log['timestamp'], datetime)
    assert isinstance(session_end_time := session_end_log['timestamp'], datetime)
    return (session_end_time - session_start_time).total_seconds()
    

def get_session_durations(logs: list[LogDict]) -> list[float]:
    """
    Return a list of durations of each SSH session in the logs.
    """
    return [session_duration for log_index, log in enumerate(logs)
            if (session_duration := get_session_duration(log_index, log, logs)) 
            is not None]
    
    
def get_global_session_stats(logs: list[LogDict]) -> tuple[float, float]:
    """
    Return the mean and standard deviation of the durations 
    of all SSH sessions.
    """
    session_durations = get_session_durations(logs)
    try:
        return (round(statistics.mean(session_durations), ndigits=2), 
                round(statistics.stdev(session_durations), ndigits=2))
    except:
        print('Error calculating statistics.')
        return 0, 0
        
        
def get_session_stats_per_user(logs: list[LogDict]) -> dict[str, tuple[float, float]]:
    """
    Return a dictionary with the mean and standard deviation 
    of the durations of all SSH sessions for each user.
    """
    session_durations = defaultdict(list)
    for log_index, log in enumerate(logs):
        if ((user := get_user_from_log(log)) is None or
            (session_duration := get_session_duration(log_index, log, logs)) is None):
            continue
        session_durations[user].append(session_duration)
        
    user_stats = {}
    for user, session_durations in session_durations.items():
        try:
            user_stats[user] = (round(statistics.mean(session_durations), ndigits=2), 
                                round(statistics.stdev(session_durations), ndigits=2))
        except:
            user_stats[user] = (session_durations[0], 0)

    return user_stats
    
    
if __name__ == '__main__':
    logs = get_log_dicts('SSH.log')
    print(get_global_session_stats(logs))
    print(get_session_stats_per_user(logs))