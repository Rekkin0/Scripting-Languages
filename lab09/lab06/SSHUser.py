import re
from datetime import datetime
from typing import Pattern


USERNAME_REGEX: Pattern[str] = re.compile(r"^[a-z_][a-z0-9_-]{0,31}$")

class SSHUser:
    def __init__(self, username: str, last_login: str):
        self.username:        str = username
        self.last_login: datetime = datetime.strptime(last_login, '%d/%m/%Y %H:%M:%S')

    def validate(self) -> bool:
        """
        Validate the username.
        """
        return USERNAME_REGEX.match(self.username) is not None
    
    def __str__(self) -> str:
        return f'{self.username} [{self.last_login}]'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(user_name={self.username}, ' \
               f'last_login={self.last_login})'
