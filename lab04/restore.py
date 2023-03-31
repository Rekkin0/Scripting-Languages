import sys, subprocess, csv
from utils import BACKUP_DIR, JOURNAL, get_timestamp
from pathlib import Path


def select_backup() -> str:
    with open(JOURNAL, "r") as file:
        journal = list(csv.DictReader(file))
    
    print("Archived backups (most recent first):")
    for i, entry in enumerate(journal[::-1]):
        timestamp = get_timestamp(entry['backup_name'])
        print(f"[{i+1}]: \
              \n\t{timestamp} \
              \n\t{entry['dirpath']} \
              \n\t{entry['backup_name']}")
        
    selection = int(input("\nChoose a backup to restore: "))
    try:
        return journal[-selection]['backup_name']
    except:
        raise Exception("Invalid selection")
    
    
def cleanup_dir(dir: Path) -> None:
    for file in dir.iterdir():
        if file.is_dir():
            cleanup_dir(file)
            file.rmdir()
        else:
            file.unlink()
            
            
def unzip_backup(dir: Path, backup_name: str) -> None:
    backup = BACKUP_DIR / backup_name
    subprocess.run(['unzip', '-q', backup, '-d', dir], cwd=BACKUP_DIR)


def restore_backup(dir: Path) -> None:
    backup_name = select_backup()
    cleanup_dir(dir)
    unzip_backup(dir, backup_name)
    print(f"Backup {backup_name} successfully restored to {dir}")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        dir = Path.cwd()
    else:
        dir = Path(sys.argv[1]).expanduser().resolve()
        if not dir.is_dir():
            raise Exception(f"{dir} is not a directory") 
    restore_backup(dir)
    
 