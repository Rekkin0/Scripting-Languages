import os, sys
from pathlib import Path


def get_path_dirs() -> list[Path]:
    """
    Returns a list of the directories in the PATH environment variable.
    """
    path_env = os.getenv('PATH')
    if path_env is None:
        raise Exception('PATH environment variable not set')
    path_dirs = path_env.split(os.pathsep)
    
    return [Path(dir).expanduser().resolve() for dir in path_dirs]
    

def is_executable(file: Path) -> bool:
    """
    Checks whether a file is executable.
    """
    return os.access(file, os.X_OK)


def get_path_dirs_with_exes() -> list[tuple[Path, list[str]]]:
    """
    Returns a list of tuples containing the directories in the PATH environment 
    variable and the executables in each directory.
    """
    path_dirs_with_exes = []
    for dir in get_path_dirs():
        exes = [file.name for file in dir.iterdir() if is_executable(file)]
        path_dirs_with_exes.append((dir, exes))
    return path_dirs_with_exes
        
        
def do_optional(option: str) -> None:
    if option == '-h' or option == '--help':
        print('Usage: path.py [OPTION]')
        print('List the directries of the PATH environment variable.\n')
        print('Options:')
        print('  -x, --executables  include the executables in each directory')
        print('  -h, --help         display this help and exit')
    elif option == '-x' or option == '--executables':
        for dir, exes in get_path_dirs_with_exes():
            print(dir, ':', sep='')
            print(*exes, sep='  ', end='\n\n')
    else:
        print(f"path.py: invalid option -- '{option}'")
        print("Try 'path.py --help' for more information.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(*get_path_dirs(), sep='\n')
    else:
        do_optional(sys.argv[1])

    