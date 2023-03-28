import os, sys, subprocess, json
from pathlib import Path
from datetime import datetime


BACKUPS_DIR = Path(os.getenv("BACKUPS_DIR") or "~/.backups").expanduser().resolve()


def choose_backup():
        
    journal = Path(BACKUPS_DIR) / "journal.json"
    with open(journal, "r") as file:
        journal_data = json.load(file)
    
    print("Archived backups (most recent first):")
    for i, entry in enumerate(journal_data[::-1]):
        date_time = datetime.strptime(entry['timestamp'], "%Y-%m-%d_%H-%M-%S").strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{i+1}]: \
              \n\t{date_time} \
              \n\t{entry['dirpath']} \
              \n\t{entry['filename']}")
        
    choice = int(input("\nChoose a backup to restore: "))
    return journal_data[-choice]['filename']


def restore_backup(backup_name: str):
    
    if len(sys.argv) <= 1:
        dirpath = Path.cwd()
    else:
        dirpath = Path(sys.argv[1]).expanduser().resolve()
        if not dirpath.is_dir():
            raise Exception(f"{dirpath} is not a directory")
        
    backup = BACKUPS_DIR / backup_name
    for file in dirpath.glob("*"):
        file.unlink()
    subprocess.run(["tar", "-C", dirpath, "-zxf", backup])


if __name__ == "__main__":
        
    backup_name = choose_backup()
    restore_backup(backup_name)
 