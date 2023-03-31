import os, re
from pathlib import Path
from datetime import datetime


DEFAULT_BACKUP_DIR = '~/.backups'
BACKUP_ENVAR = os.getenv('BACKUP_DIR')
BACKUP_DIR = Path(BACKUP_ENVAR or DEFAULT_BACKUP_DIR).expanduser().resolve()

FILE_TIMESTAMP = '%Y-%m-%d_%H-%M-%S'
JOURNAL_TIMESTAMP = '%d %b %Y %H:%M:%S'
BACKUP_EXTENSION = 'zip'

JOURNAL = BACKUP_DIR / 'journal.csv'
FIELDNAMES = ('timestamp', 'dirpath', 'backup_name')

REGEX = re.compile(r'(.+)-.+')
def get_timestamp(filename: str) -> datetime:
    timestamp = REGEX.match(filename)
    if not timestamp:
        raise Exception(f'Invalid filename: {filename}')
    return datetime.strptime(timestamp.group(1), FILE_TIMESTAMP)