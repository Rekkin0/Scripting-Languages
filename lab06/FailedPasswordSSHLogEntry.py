import re
from typing import Match

from SSHLogEntry import SSHLogEntry


FAILED_PASSWORD_REGEX = re.compile(r'Failed password for (?P<user_invalid>invalid user )*(?P<username>\w+)')

class FailedPasswordSSHLogEntry(SSHLogEntry):
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
        return False if self.match is None \
            else self.match.group('user_invalid') is None
    
    def validate(self) -> bool:
        """
        Validate the log entry.
        """
        return self.match is not None
    
if __name__ == '__main__':
    entry = FailedPasswordSSHLogEntry('Dec 10 11:03:41 LabSZ sshd[25453]: Failed password for root from 183.62.140.253 port 52762 ssh2')
    entry_invalid = FailedPasswordSSHLogEntry('Dec 10 11:03:39 LabSZ sshd[25448]: Failed password for invalid user admin from 103.99.0.122 port 60150 ssh2')
    bad_entry = FailedPasswordSSHLogEntry('Dec 10 09:31:34 LabSZ sshd[24678]: Connection closed by 104.192.3.34 [preauth]')
    
    print(entry)
    print('validate:', entry.validate(), 'valid_user:', entry.is_user_valid(), 'username:', entry.get_username())
    print(entry_invalid)
    print('validate:', entry_invalid.validate(), 'valid_user:', entry_invalid.is_user_valid(), 'username:', entry_invalid.get_username())
    print(bad_entry)
    print('validate:', bad_entry.validate(), 'valid_user:', bad_entry.is_user_valid(), 'username:', bad_entry.get_username())
