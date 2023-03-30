import os, sys, subprocess, csv
from pathlib import Path
from datetime import datetime


BACKUPS_DIR = Path(os.getenv("BACKUPS_DIR") or "~/.backups").expanduser().resolve()


def choose_backup():
        
    journal = Path(BACKUPS_DIR) / "journal.csv"
    with open(journal, "r") as file:
        journal_data = list(csv.DictReader(file))
    
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
    
    for root, dirs, files in os.walk(dirpath, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    backup = BACKUPS_DIR / backup_name
    subprocess.run(["unzip", "-q", backup, "-d", dirpath], cwd=BACKUPS_DIR)


if __name__ == "__main__":
        
    backup_name = choose_backup()
    restore_backup(backup_name)
 