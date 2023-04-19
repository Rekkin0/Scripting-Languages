from datetime import datetime
from ipaddress import IPv4Address
from typing import Iterator

from SSHLogEntry import SSHLogEntry
from AcceptedPasswordSSHLogEntry import AcceptedPasswordSSHLogEntry, ACCEPTED_PASSWORD_REGEX
from FailedPasswordSSHLogEntry import FailedPasswordSSHLogEntry, FAILED_PASSWORD_REGEX
from ErrorSSHLogEntry import ErrorSSHLogEntry, ERROR_REGEX
from OtherSSHLogEntry import OtherSSHLogEntry


class SSHLogJournal:
    def __init__(self) -> None:
        self.entries = []

    def __len__(self) -> int:
        return len(self.entries)

    def __contains__(self, entry: SSHLogEntry) -> bool:
        return entry in self.entries

    def __iter__(self) -> Iterator[SSHLogEntry]:
        return iter(self.entries)
    
    def create_entry(self, log: str) -> SSHLogEntry:
        """
        Create a log entry based on the log message.
        """
        if ACCEPTED_PASSWORD_REGEX.search(log) is not None:
            return AcceptedPasswordSSHLogEntry(log)
        if FAILED_PASSWORD_REGEX.search(log) is not None:
            return FailedPasswordSSHLogEntry(log)
        if ERROR_REGEX.search(log) is not None:
            return ErrorSSHLogEntry(log)
        
        return OtherSSHLogEntry(log)

    def append(self, log: str) -> None:
        """
        Append a log entry to the journal.
        """
        entry = self.create_entry(log)
        if entry.validate():
            self.entries.append(entry)


    def get_entry(self, index: int) -> SSHLogEntry:
        """
        Get the log entry at the given index.
        """
        return self.entries[index]

    def get_entries_by_ipv4(self, ipv4: str) -> list[SSHLogEntry]:
        """
        Get all log entries that contain the given IPv4 address.
        """
        try:
            return [entry for entry in self.entries 
                    if entry.get_ipv4() == IPv4Address(ipv4)]
        except:
            raise SystemExit('Invalid IPv4 address')
    
    def get_entries_in_time_range(self, start: str, end: str) -> list[SSHLogEntry]:
        """
        Get all log entries that are in the given time range.
        """
        try:
            start_date = datetime.strptime(start, '%d/%m')
            end_date   = datetime.strptime(end, '%d/%m')
            
            return [entry for entry in self.entries 
                    if start_date <= entry.timestamp <= end_date]
        except:
            raise SystemExit('Invalid date')
