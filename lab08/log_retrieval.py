# aggregation
from pathlib import Path


def file_exists(file_path: str) -> bool:
    """
    Return True if the file exists, False otherwise.
    """
    return (Path(__file__).parent / file_path).is_file()


def get_lines(file_path: str) -> list[str]:
    """
    Return a list of lines in a file.
    """
    if not file_exists(file_path):
        raise FileNotFoundError
        
    with open(file_path) as file:
        return file.readlines()
