import random

from exc1 import get_log_dicts
from exc2 import LogDict, get_user_from_log


def get_unique_users(logs: list[LogDict]) -> list[str]:
    """
    Return a list of all unique users in the logs.
    """
    return list({user for log in logs 
                 if (user := get_user_from_log(log)) is not None})
    
    
def get_logs_of_user(logs: list[LogDict], user: str) -> list[LogDict]:
    """
    Return a list of all logs of a user.
    """
    return [log for log in logs 
            if get_user_from_log(log) == user]


def get_n_random_logs_from_random_user(logs: list[LogDict], n: int) -> list[LogDict]:
    """
    Return a list of n random logs from a random user 
    in the logs.
    """
    users = get_unique_users(logs)
    random_user = random.choice(users)
    user_logs = get_logs_of_user(logs, random_user)
    
    return random.sample(user_logs, n)


if __name__ == '__main__':
    logs = get_log_dicts('SSH.log')
    print(get_n_random_logs_from_random_user(logs, 3))