import sys, subprocess, csv
from utils import *
from pathlib import Path
from datetime import datetime


def get_backup_name(dir: Path) -> str:
    """
    Generates for a backup archive of a directory based on the current 
    time and date.
    """
    timestamp = datetime.now().strftime(FILE_TIMESTAMP)
    
    return f'{timestamp}-{dir.name}.{BACKUP_EXTENSION}'


def archive_backup(dir: Path, backup_name: str) -> None:
    """
    Archives the contents of a directory into a zip file.
    """
    command = ['zip', '-qr', backup_name, '.']
    subprocess.run(command, cwd=dir)
    

def move_backup(dir: Path, backup_name: str) -> None:
    """
    Moves a backup archive to the backup directory.
    """
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    command = ['mv', backup_name, BACKUP_DIR]
    subprocess.run(command, cwd=dir)


def update_journal(dir: Path, backup_name: str) -> None:
    """
    Updates the journal file with the details of a backup.
    """
    timestamp = get_timestamp(backup_name).strftime(JOURNAL_TIMESTAMP)
    entry_values = (timestamp, dir, backup_name)
    entry = dict(zip(FIELD_NAMES, entry_values))
    
    journal_exists = JOURNAL.is_file()
    with open(JOURNAL, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        if not journal_exists:
            writer.writeheader()
        writer.writerow(entry)  


def create_backup(dir: Path) -> None:
    """
    Creates a backup of a directory.
    """
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