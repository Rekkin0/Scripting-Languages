import os, sys, subprocess, json
from pathlib import Path
from datetime import datetime


BACKUPS_DIR = Path(os.getenv("BACKUPS_DIR") or "~/.backups").expanduser().resolve()


def create_backup() -> str:
    
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)
        
    dirpath = Path(sys.argv[1]).expanduser().resolve()
    if not dirpath.is_dir():
        raise Exception(f"{dirpath} is not a directory")
        
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    extension = 'tar.gz'
    backup_name = f"{timestamp}-{dirpath.name}.{extension}"
    
    subprocess.run(["tar", "-C", dirpath, "-zcf", backup_name, "."])
    subprocess.run(["mv", backup_name, BACKUPS_DIR])
    
    return backup_name
    

def journal_backup(backup_name: str) -> None:
    
    journal = Path(BACKUPS_DIR) / "journal.json"
    journal.touch(exist_ok=True)
    
    entry = {
        "timestamp": backup_name[:19],
        "dirpath"  : str(Path(sys.argv[1]).expanduser().resolve()),
        "filename" : backup_name
    }
      
    journal_data = []
    with open(journal, "r") as file:
        try:
            journal_data = json.load(file)
        except json.decoder.JSONDecodeError:
            pass
    
    journal_data.append(entry)
    with open(journal, "w") as file:
        json.dump(journal_data, file, indent=4)   
    

if __name__ == "__main__":
        
    backup_name = create_backup()
    journal_backup(backup_name)