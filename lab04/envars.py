import os, sys


if __name__ == "__main__":
    
    envars = sorted(os.environ.items())
    
    for key, value in envars:
        if len(sys.argv) <= 1 or key in sys.argv[1:]:
            print(key, "=", value)
    