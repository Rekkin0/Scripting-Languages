from pathlib import Path


def db_exists(db_name: str) -> Path:
    """
    Check if the database exists.
    """
    db_file: Path = Path(f'{db_name}.sqlite3').resolve()
    if not db_file.is_file():
        raise SystemExit(f'Database "{db_name}.sqlite3" does not exist.')
    return db_file

def db_not_exists(db_name: str) -> str:
    """
    Check if the database does not exist.
    """
    db_file: Path = Path(f'{db_name}.sqlite3').resolve()
    if db_file.is_file():
        raise SystemExit(f'Database "{db_name}.sqlite3" already exists.')
    return db_name

def file_exists(file_path: str) -> Path:
    """
    Check if the file exists.
    """
    file: Path = Path(file_path).resolve()
    if not file.is_file():
        raise SystemExit(f'File "{file_path}" does not exist.')
    return file
