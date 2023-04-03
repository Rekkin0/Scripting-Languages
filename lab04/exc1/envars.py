import os, sys


def print_envars(filters: list[str]) -> None:
    """
    Prints all environment variables or only those specified in 
    the filter list (if it exists).
    """
    if are_filters := len(filters) > 1:
        filters = [filter.upper() for filter in filters[1:]]
    envars = os.environ.items()
    for envar, value in sorted(envars):
        if not are_filters or envar in filters:
            print(envar, "=", value)


if __name__ == '__main__':
    print_envars(sys.argv)