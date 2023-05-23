import pytest

from src.SSHLogEntry import SSHLogEntry

class TestDatetime:
    from datetime import datetime
    
    def test_valid(self) -> None:
        log: str = 'Dec 10 06:55:46 LabSZ sshd[24200]: Invalid user webmaster from 173.234.31.186'
        assert SSHLogEntry(log).timestamp == self.datetime(1900, 12, 10, 6, 55, 46)
        
    def test_invalid(self) -> None:
        log: str = 'Qoi 76 45:99:78 LabSZ sshd[24200]: Invalid user webmaster from 173.234.31.186'
        with pytest.raises(SystemExit):
            SSHLogEntry(log)
            
    def test_missing(self) -> None:
        log: str = 'LabSZ sshd[24200]: Invalid user webmaster from'
        with pytest.raises(SystemExit):
            SSHLogEntry(log)


class TestIPAddress:
    from ipaddress import IPv4Address
    
    def test_valid(self) -> None:
        log: str = ('Dec 10 06:55:48 LabSZ sshd[24200]: Failed password '
                    'for invalid user webmaster from 173.234.31.186 port 38926 ssh2')
        assert SSHLogEntry(log).get_ipv4() == self.IPv4Address('173.234.31.186')
        
    def test_invalid(self) -> None:
        log: str = ('Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for '
                    'invalid user webmaster from 666.777.88.213 port 38926 ssh2')
        with pytest.raises(SystemExit):
            SSHLogEntry(log).get_ipv4()
    
    def test_missing(self) -> None:
        log: str = ('Dec 10 07:07:38 LabSZ sshd[24206]: pam_unix(sshd:auth): '
                    'check pass; user unknown')
        assert SSHLogEntry(log).get_ipv4() is None
