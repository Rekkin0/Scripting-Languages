import re
from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from datetime import datetime
from typing import Any, Pattern, Match

LogDict = dict[str, Any]

LOG_REGEX:  Pattern[str] = re.compile(r'(\w{3} {1,2}\d{1,2} \d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')
IPV4_REGEX: Pattern[str] = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
TIMESTAMP_FORMAT:    str = '%b %d %H:%M:%S'


class SSHLogEntry():
    def __init__(self, log: str) -> None:
        self.entry:     LogDict  = self.parse_log(log)
        self.bytes:     int      = self.entry['bytes']
        self.timestamp: datetime = self.entry['timestamp']
        self.hostname:  str      = self.entry['hostname']
        self.process:   int      = self.entry['process']
        self._message:  str      = self.entry['message']

    def parse_log(self, log: str) -> LogDict:
        """
        Parse a log line to a dictionary.
        """
        match: Match[str] | None = LOG_REGEX.match(log)
        if match is None:
            raise SystemExit(f'Invalid line: {log}')
        match_groups: tuple[str | Any, ...] = match.groups()
        timestamp: str | Any = match_groups[0]
        hostname:  str | Any = match_groups[1]
        process:   str | Any = match_groups[2]
        message:   str | Any = match_groups[3]
    
        try: 
        return {
            'bytes'    : len(log),
            'timestamp': datetime.strptime(timestamp, TIMESTAMP_FORMAT),
            'hostname' : hostname,
            'process'  : int(process),
            'message'  : message
        }
        
    def get_ipv4(self) -> IPv4Address | None:
        """
        Return an IPv4Address object if the log entry 
        contains an IPv4 address, None otherwise.
        """
        match: Match[str] | None = IPV4_REGEX.search(self._message)  # type: ignore
        return IPv4Address(match.group(0)) if match else None
    
    @property
    def has_ipv4(self) -> bool:
        """
        Return True if the log entry contains an IPv4 address, False otherwise.
        """
        return self.get_ipv4() is not None
    
    @abstractmethod
    def validate(self) -> bool:
        """
        Validate the log entry.
        """
        raise NotImplementedError
    
    def __str__(self) -> str:
        timestamp: str = self.timestamp.strftime(TIMESTAMP_FORMAT)  # type: ignore
        return f'[{timestamp}] [{self.hostname}] [{self.process}] {self._message}'
    
    def __repr__(self) -> str:
        timestamp: str = self.timestamp.strftime(TIMESTAMP_FORMAT)  # type: ignore
        return f'{self.__class__.__name__}(bytes={self.bytes}, ' \
               f'timestamp={timestamp}, hostname={self.hostname}, ' \
               f'process={self.process}, message={self._message})'
               
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, SSHLogEntry):
            return NotImplemented
        return self.__dict__ == other.__dict__
    
    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, SSHLogEntry):
            return NotImplemented
        return self.timestamp < other.timestamp  # type: ignore
    
    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, SSHLogEntry):
            return NotImplemented
        return self.timestamp > other.timestamp  # type: ignore
    