import os, sys, subprocess, csv
from pathlib import Path
from datetime import datetime


BACKUPS_DIR = Path(os.getenv("BACKUPS_DIR") or "~/.backups").expanduser().resolve()


def create_backup() -> str:
    
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)
        
    dirpath = Path(sys.argv[1]).expanduser().resolve()
    if not dirpath.is_dir():
        raise Exception(f"{dirpath} is not a directory")
        
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    extension = 'zip'
    backup_name = f"{timestamp}-{dirpath.name}.{extension}"
    
    subprocess.run(["zip", "-qr", backup_name, ".", "-i", "*"], cwd=dirpath)
    subprocess.run(["mv", backup_name, BACKUPS_DIR], cwd=dirpath)
    
    return backup_name
    

def journal_backup(backup_name: str) -> None:
    
    journal = Path(BACKUPS_DIR) / "journal.csv"
    
    entry = {
        "timestamp": backup_name[:19],
        "dirpath"  : str(Path(sys.argv[1]).expanduser().resolve()),
        "filename" : backup_name
    }
    
    journal_exists = journal.is_file()
    
    with open(journal, "a") as file:
        writer = csv.DictWriter(file, fieldnames=entry.keys())
        if not journal_exists:
            writer.writeheader()
        writer.writerow(entry)  
    

if __name__ == "__main__":
        
    backup_name = create_backup()
    journal_backup(backup_name)