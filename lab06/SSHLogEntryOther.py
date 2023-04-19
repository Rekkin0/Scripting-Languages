import re
from SSHLogEntry import SSHLogEntry


ERROR_REGEX = re.compile(r'error: (?P<error>.+) ')

class SSHLogEntryOther(SSHLogEntry):
    def __init__(self, log: str) -> None:
        super().__init__(log)
    
    def validate(self) -> bool:
        return True