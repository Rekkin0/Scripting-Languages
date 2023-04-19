import re
from SSHLogEntry import SSHLogEntry
from typing import Match


ERROR_REGEX = re.compile(r'error: (?P<error>.+) ')

class SSHLogEntryError(SSHLogEntry):
    def __init__(self, log: str) -> None:
        super().__init__(log)
        self.match = self.match_message()
        self.error = self.get_error()
        
    def match_message(self) -> Match[str] | None:
        """
        Match the message of the log entry.
        """
        assert isinstance(self._message, str)
        return ERROR_REGEX.search(self._message)

    def get_error(self) -> str | None:
        """
        Get the error from the log entry.
        """
        return None if self.match is None \
            else self.match.group('error')
    
    def validate(self) -> bool:
        """
        Validate the log entry.
        """
        return self.match is not None