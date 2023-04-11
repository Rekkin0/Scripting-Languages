import argparse


parser = argparse.ArgumentParser(description='')
parser.add_argument('log_file', 
                    type=str, 
                    help='path to the log file')
parser.add_argument('-l', '--level', 
                    type=str, 
                    help='logging level', 
                    default='INFO', 
                    choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])

subparsers = parser.add_subparsers(dest='command', 
                                   help='sub-command help')
subparsers.add_parser