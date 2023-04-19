import re
from typing import Match

from SSHLogEntry import SSHLogEntry


ERROR_REGEX = re.compile(r'error: (?P<error>.+) ')

class ErrorSSHLogEntry(SSHLogEntry):
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
    
    
if __name__ == '__main__':
    entry = ErrorSSHLogEntry('Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]')
    bad_entry = ErrorSSHLogEntry('Dec 10 09:31:34 LabSZ sshd[24678]: Connection closed by 104.192.3.34 [preauth]')
    
    print(entry)
    print('validate:', entry.validate(), 'error:', entry.get_error())
    print(bad_entry)
    print('validate:', bad_entry.validate(), 'error:', bad_entry.get_error())