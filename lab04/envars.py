import os, sys


def print_envars(filter_list: list[str]) -> None:
    envars = os.environ.items()
    for envar, value in sorted(envars):
        if len(filter_list) <= 1 or envar in filter_list[1:]:
            print(envar, "=", value)


if __name__ == '__main__':
    print_envars(sys.argv)