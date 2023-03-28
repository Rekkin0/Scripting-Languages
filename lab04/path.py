import os, sys


def print_executables(path_dirs: list[str]) -> None:
    
    for dir in path_dirs:
        print(dir + ":")
        for file in os.scandir(dir):
            if os.access(file.path, os.X_OK):
                print(file.name, end="  ")
        print()


if __name__ == "__main__":
    
    path_env = os.getenv("PATH")
    if path_env is None:
        raise Exception("PATH environment variable not set")
    
    path_dirs = path_env.split(os.pathsep)
    
    param = sys.argv[1] if len(sys.argv) > 1 else None
    if param is None:
        print(*path_dirs, sep="\n")
    elif param == "-x" or param == "--executables":
        print_executables(path_dirs)
    elif param == "-h" or param == "--help":
        print("Usage: path.py [OPTION]")
        print("List the directries of the PATH environment variable.\n")
        print("  -x, --executables  include the executables in each directory")
        print("  -h, --help         display this help and exit")
    else:
        print(f"path.py: invalid option -- '{param}'")
        print("Try 'path.py --help' for more information.")
    