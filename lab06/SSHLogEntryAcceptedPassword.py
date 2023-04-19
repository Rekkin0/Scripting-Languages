import re
from SSHLogEntry import SSHLogEntry
from typing import Match


ACCEPTED_PASSWORD_REGEX = re.compile(r'Accepted password for (?P<username>\w+)')

class SSHLogEntryAcceptedPassword(SSHLogEntry):
    def __init__(self, log: str) -> None:
        super().__init__(log)
        self.match = self.match_message()
        self.username = self.get_username()
        
    def match_message(self) -> Match[str] | None:
        """
        Match the message of the log entry.
        """
        assert isinstance(self._message, str)
        return ACCEPTED_PASSWORD_REGEX.search(self._message)

    def get_username(self) -> str | None:
        """
        Get the username from the log entry.
        """
        return None if self.match is None \
            else self.match.group('username')
    
    def validate(self) -> bool:
        """
        Validate the log entry.
        """
        return self.match is not None