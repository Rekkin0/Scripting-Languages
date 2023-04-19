import re

from SSHLogEntry import SSHLogEntry


class OtherSSHLogEntry(SSHLogEntry):
    def __init__(self, log: str) -> None:
        super().__init__(log)
    
    def validate(self) -> bool:
        return True
    
    
if __name__ == '__main__':
    entry = OtherSSHLogEntry('Dec 10 09:31:34 LabSZ sshd[24678]: Connection closed by 104.192.3.34 [preauth]')
    
    print(entry)
    print(entry.validate())