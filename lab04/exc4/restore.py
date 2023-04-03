import sys, subprocess, csv
from utils import BACKUP_DIR, JOURNAL, get_timestamp
from pathlib import Path


def select_backup() -> str:
    """
    Prompts the user to select a backup from the ones listed 
    in the journal file.
    """
    with open(JOURNAL, "r") as file:
        journal = list(csv.DictReader(file))
    
    print("Archived backups (most recent first):")
    for i, entry in enumerate(journal[::-1]):
        timestamp = get_timestamp(entry['backup_name'])
        print(f"[{i+1}]: \
              \n\t{timestamp} \
              \n\t{entry['dirpath']} \
              \n\t{entry['backup_name']}")
    print(f"[{len(journal)+1}]: Cancel")
    
    while True:
        try:
            selection = int(input("\nChoose a backup to restore: "))
            if selection == len(journal)+1:
                break
            return journal[-selection]['backup_name']
        except:
            print("Invalid selection.")
            
    exit()
    
    
def clear_dir(dir: Path) -> None:
    """
    Clears the contents of a directory.
    """
    for file in dir.iterdir():
        if file.is_dir():
            clear_dir(file)
            file.rmdir()
        else:
            file.unlink()
            
            
def unzip_backup(dir: Path, backup_name: str) -> None:
    """
    Unzips a backup archive into a directory.
    """
    command = ['unzip', '-q', backup_name, '-d', dir]
    subprocess.run(command, cwd=BACKUP_DIR)


def restore_backup(dir: Path) -> None:
    """
    Restores a backup to a directory.
    """
    backup_name = select_backup()
    clear_dir(dir)
    unzip_backup(dir, backup_name)
    print(f"Backup {backup_name} successfully restored to {dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        dir = Path.cwd()
    else:
        dir = Path(sys.argv[1]).expanduser().resolve()
        if not dir.is_dir():
            raise Exception(f"{dir} is not a directory") 
    restore_backup(dir)
    
 