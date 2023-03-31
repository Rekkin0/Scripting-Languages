import sys, subprocess, csv
from utils import BACKUP_DIR, FILE_TIMESTAMP, JOURNAL_TIMESTAMP, BACKUP_EXTENSION, JOURNAL, FIELDNAMES, get_timestamp
from pathlib import Path
from datetime import datetime


def get_backup_name(dir: Path) -> str:
    timestamp = datetime.now().strftime(FILE_TIMESTAMP)
    
    return f'{timestamp}-{dir.name}.{BACKUP_EXTENSION}'


def archive_backup(dir: Path, backup_name: str) -> None:
    subprocess.run(['zip', '-qr', backup_name, '.'], cwd=dir)
    

def move_backup(dir: Path, backup_name: str) -> None:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(['mv', backup_name, BACKUP_DIR], cwd=dir)


def update_journal(dir: Path, backup_name: str) -> None:
    timestamp = get_timestamp(backup_name).strftime(JOURNAL_TIMESTAMP)
    entry_values = (timestamp, dir, backup_name)
    entry = dict(zip(FIELDNAMES, entry_values))
    
    journal_exists = JOURNAL.is_file()
    with open(JOURNAL, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        if not journal_exists:
            writer.writeheader()
        writer.writerow(entry)  


def create_backup(dir: Path) -> None:
    backup_name = get_backup_name(dir)
    archive_backup(dir, backup_name)
    move_backup(dir, backup_name)
    update_journal(dir, backup_name)
    print(f'Backup {backup_name} successfully created in {BACKUP_DIR}')


if __name__ == '__main__':
    dir = Path(sys.argv[1]).expanduser().resolve()
    if not dir.is_dir():
        raise Exception(f'{dir.name} is not a directory. Cannot backup.')
    create_backup(dir)