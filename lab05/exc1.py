# aggregation
from pathlib import Path

from exc2 import LogDict, parse_log


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
        print(f'File {file_path} does not exist.')
        exit()
        
    with open(file_path) as file:
        return file.readlines()


def get_log_dicts(file_path: str) -> list[LogDict]:
    """ 
    Return a list of log dictionaries in a file. 
    """
    if not file_exists(file_path):
        print(f'File {file_path} does not exist.')
        exit()
    
    return [parse_log(line) for line in get_lines(file_path)]
    
    
if __name__ == '__main__':
    # print(*get_lines('SSH.log'))
    print(*get_log_dicts('SSH.log'), sep='\n')
    pass