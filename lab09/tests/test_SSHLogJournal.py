import pytest

from src.SSHLogJournal import SSHLogJournal
from src.SSHLogEntry import SSHLogEntry
from src.AcceptedPasswordSSHLogEntry import AcceptedPasswordSSHLogEntry
from src.FailedPasswordSSHLogEntry import FailedPasswordSSHLogEntry
from src.ErrorSSHLogEntry import ErrorSSHLogEntry
from src.OtherSSHLogEntry import OtherSSHLogEntry
        

class TestEntryType:
    journal = SSHLogJournal()
    
    @pytest.mark.parametrize('log, entry_type', [
        ('Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from', AcceptedPasswordSSHLogEntry),
        ('Dec 10 09:31:34 LabSZ sshd[24678]: Failed password for root from', FailedPasswordSSHLogEntry),
        ('Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from', ErrorSSHLogEntry),
        ('Dec 10 09:31:34 LabSZ sshd[24678]: Connection closed by', OtherSSHLogEntry)
    ])
    def test_valid(self, log: str, entry_type) -> None:
        self.journal.append(log)
        assert isinstance(self.journal[len(self.journal)-1], entry_type)
    
    def test_invalid(self) -> None:
        log = 'efjgiosdihfgohe;fdgf'
        with pytest.raises(SystemExit):
            self.journal.append(log)
