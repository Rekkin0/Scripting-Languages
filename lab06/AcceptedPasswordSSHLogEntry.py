import re
from typing import Match

from SSHLogEntry import SSHLogEntry


ACCEPTED_PASSWORD_REGEX = re.compile(r'Accepted password for (?P<username>\w+)')

class AcceptedPasswordSSHLogEntry(SSHLogEntry):
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
    

if __name__ == '__main__':
    entry = AcceptedPasswordSSHLogEntry('Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2')
    bad_entry = AcceptedPasswordSSHLogEntry('Dec 10 09:31:34 LabSZ sshd[24678]: Connection closed by 104.192.3.34 [preauth]')
    
    print(entry)
    print('validate:', entry.validate(), 'username:', entry.get_username())
    print(bad_entry)
    print('validate:', bad_entry.validate(), 'username:', bad_entry.get_username())