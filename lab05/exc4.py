import random
from pathlib import Path

from utils import LOG_PATH
from exc1 import get_log_dicts, LogDict
from exc2 import get_user_from_log


def get_users_from_logs(logs: list[LogDict]) -> set[str]:
    """
    Return a set of all unique users in the logs.
    """
    return set(user for log in logs if (user := get_user_from_log(log)) is not None)

def get_n_logs_from_random_user(logs: list[LogDict], n: int) -> list[LogDict]:
    """
    Return a list of n logs from a random user in the logs.
    """
    users = get_users_from_logs(logs)
    random_user = random.choice(list(users))
    user_logs = [log for log in logs if get_user_from_log(log) == random_user]
    
    return random.sample(user_logs, n)

def get_user_login_count(logs: list[LogDict]) -> dict[str, int]:
    """
    Return a dictionary with the number of logins for each user.
    """
    users = get_users_from_logs(logs)
    return {user: len([log for log in logs if get_user_from_log(log) == user]) for user in users}

