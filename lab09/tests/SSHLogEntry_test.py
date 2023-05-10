from lab06.SSHLogEntry import SSHLogEntry
from datetime import datetime


def test_datetime_parsing():
    log = 'Dec 10 06:55:46 LabSZ sshd[24200]: Invalid user webmaster from 173.234.31.186'
    entry = SSHLogEntry(log)
    assert entry.timestamp == datetime(1900, 12, 10, 6, 55, 46)
    ...
    
def test_datetime_parsing_fail():
    log = 'Qoi 76 45:99:78 LabSZ sshd[24200]: Invalid user webmaster from 173.234.31.186'
    entry = SSHLogEntry(log)
    print(entry.timestamp)
    

if __name__ == '__main__':
    test_datetime_parsing_fail()