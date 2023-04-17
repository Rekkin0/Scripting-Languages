import re
from abc import ABC, abstractmethod
from ipaddress import IPv4Address
from datetime import datetime
from typing import Any

LogDict = dict[str, datetime | int | str]

LOG_REGEX  = re.compile(r'(\w{3} {1,2}\d{1,2} \d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.+)')
IPV4_REGEX = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
TIMESTAMP_FORMAT = '%b %d %H:%M:%S'


class SSHLogEntry():
    def __init__(self, line: str) -> None:
        self.log       = self.parse_log(line)
        self.bytes     = self.log['bytes']
        self.timestamp = self.log['timestamp']
        self.hostname  = self.log['hostname']
        self.process   = self.log['process']
        self.__message = self.log['message']

    def parse_log(self, line: str) -> LogDict:
        """
        Parse a log line to a dictionary.
        """
        match = LOG_REGEX.match(line)
        if match is None:
            raise SystemExit(f'Invalid line: {line}')
        timestamp, hostname, process, message = match.groups()
    
        return {
            'bytes'    : len(line),
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
        match = IPV4_REGEX.search(self.__message)  # type: ignore
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
        timestamp = self.timestamp.strftime(TIMESTAMP_FORMAT)  # type: ignore
        return f'[{timestamp}] [{self.hostname}] [{self.process}] {self.__message}'
    
    def __repr__(self) -> str:
        timestamp = self.timestamp.strftime(TIMESTAMP_FORMAT)  # type: ignore
        return f'{self.__class__.__name__}(bytes={self.bytes}, ' \
               f'timestamp={timestamp}, hostname={self.hostname}, ' \
               f'process={self.process}, message={self.__message})'
               
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