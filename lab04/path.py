import os, sys
from pathlib import Path


def get_path_dirs() -> list[Path]:
    path_env = os.getenv('PATH')
    if path_env is None:
        raise Exception('PATH environment variable not set')
    path_dirs = path_env.split(os.pathsep)
    
    return [Path(dir).expanduser().resolve() for dir in path_dirs]
    

def is_executable(file: Path) -> bool:
    return os.access(file, os.X_OK)


def print_executables(path_dirs: list[Path]) -> None:
    for dir in path_dirs:
        print(dir, ':', sep='')
        [print(file.name, end='  ') for file in dir.iterdir() if is_executable(file)]
        print('\n' + '_' * 70)     
        
        
def do_optional(option: str, path_dirs: list[Path]) -> None:
    if option == '-h' or option == '--help':
        print('Usage: path.py [OPTION]')
        print('List the directries of the PATH environment variable.\n')
        print('Options:')
        print('  -x, --executables  include the executables in each directory')
        print('  -h, --help         display this help and exit')
    elif option == '-x' or option == '--executables':
        print_executables(path_dirs)
    else:
        print(f"path.py: invalid option -- '{option}'")
        print("Try 'path.py --help' for more information.")


if __name__ == '__main__':
    path_dirs = get_path_dirs()
    if len(sys.argv) <= 1:
        print(*path_dirs, sep='\n')
    else:
        do_optional(sys.argv[1], path_dirs)

    