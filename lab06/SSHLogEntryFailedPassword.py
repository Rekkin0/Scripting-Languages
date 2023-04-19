import re
from SSHLogEntry import SSHLogEntry
from typing import Match


FAILED_PASSWORD_REGEX = re.compile(r'Failed password for (?P<user_invalid>invalid user)* (?P<username>\w+)')

class SSHLogEntryFailedPassword(SSHLogEntry):
    def __init__(self, log: str) -> None:
        super().__init__(log)
        self.match = self.match_message()
        self.username = self.get_username()
        self.valid_user = self.is_user_valid()
        
    def match_message(self) -> Match[str] | None:
        """
        Match the message of the log entry.
        """
        assert isinstance(self._message, str)
        return FAILED_PASSWORD_REGEX.search(self._message)

    def get_username(self) -> str | None:
        """
        Get the username from the log entry.
        """
        return None if self.match is None \
            else self.match.group('username')
    
    def is_user_valid(self) -> bool:
        """
        Check if the username is of a valid user.
        """
        return True if self.match is None \
            else self.match.group('user_invalid') is None
    
    def validate(self) -> bool:
        """
        Validate the log entry.
        """
        return self.match is not None