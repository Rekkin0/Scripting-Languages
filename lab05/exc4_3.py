from collections import Counter

from exc1 import get_log_dicts
from exc2 import LogDict, get_user_from_log


def get_users(logs: list[LogDict]) -> list[str]:
    """
    Return a list of all users (with a record of a user 
    for its each occurence in the logs).
    """
    return [user for log in logs 
            if (user := get_user_from_log(log)) is not None]


def get_most_and_least_active_users(logs: list[LogDict]) -> tuple[list[str], list[str]]:
    """
    Return a tuple of two lists, with the least and most active 
    users respectively (in terms of frequency of logging in).
    """
    # returns a list of tuples with users and their login counts, 
    # sorted by login frequency (ascending).
    users = Counter(get_users(logs)).most_common()
    min_login_count, max_login_count = users[-1][1], users[0][1]
    
    min_users = []
    for user, login_count in reversed(users):
        if login_count > min_login_count:
            break
        min_users.append(user)
        
    max_users = []
    for user, login_count in users:
        if login_count < max_login_count:
            break
        max_users.append(user)
        
    return (min_users, max_users)


if __name__ == '__main__':
    logs = get_log_dicts('SSH.log')
    print(get_most_and_least_active_users(logs))