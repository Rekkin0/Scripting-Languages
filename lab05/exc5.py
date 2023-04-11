import argparse

from exc1 import get_log_dicts
from exc2 import parse_log, get_ipv4s_from_log, get_user_from_log, get_message_type
from exc3 import set_logging_level, log_entry
from exc4_1 import get_n_random_logs_from_random_user
from exc4_2 import get_global_session_stats, get_session_stats_per_user
from exc4_3 import get_most_and_least_active_users


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


def parse_log_command():
    print(parse_log(args.log_line))

parse_log_parser = subparsers.add_parser('parse-log')
parse_log_parser.add_argument('log_line',
                              type=str,
                              help='log line to parse')
parse_log_parser.set_defaults(func=parse_log_command)


def get_ipv4s_from_log_command():
    print(get_ipv4s_from_log(parse_log(args.log_line)))
    
get_ipv4s_from_log_parser = subparsers.add_parser('ipv4s')
get_ipv4s_from_log_parser.add_argument('log_line',
                                       type=str,
                                       help='log line to parse')
get_ipv4s_from_log_parser.set_defaults(func=get_ipv4s_from_log_command)


def get_user_from_log_command():
    print(get_user_from_log(parse_log(args.log_line)))
    
get_user_from_log_parser = subparsers.add_parser('user')
get_user_from_log_parser.add_argument('log_line',
                                      type=str,
                                      help='log line to parse')
get_user_from_log_parser.set_defaults(func=get_user_from_log_command)


def get_message_type_command():
    assert isinstance(message := parse_log(args.log_line)['message'], str)
    print(get_message_type(message))
    
get_message_type_parser = subparsers.add_parser('message-type')
get_message_type_parser.add_argument('log_line',
                                     type=str,
                                     help='log line to parse')
get_message_type_parser.set_defaults(func=get_message_type_command)


def log_entries_command():
    set_logging_level(args.level)
    [log_entry(log) for log in get_log_dicts(args.log_file)]

log_entries_parser = subparsers.add_parser('log-entries')
log_entries_parser.set_defaults(func=log_entries_command)


def get_n_random_logs_from_random_user_command():
    log_dicts = get_log_dicts(args.log_file)
    print(*get_n_random_logs_from_random_user(log_dicts, args.log_count), sep='\n')
    
get_n_random_logs_from_random_user_parser = subparsers.add_parser('random-logs')
get_n_random_logs_from_random_user_parser.add_argument('log_count',
                                                       type=int,
                                                       help='number of logs to return')
get_n_random_logs_from_random_user_parser.set_defaults(func=get_n_random_logs_from_random_user_command)


def get_global_session_stats_command():
    mean, std_dev = get_global_session_stats(get_log_dicts(args.log_file))
    print(f'MEAN: {mean}\nSTD DEV: {std_dev}')
    
get_global_session_stats_parser = subparsers.add_parser('global-stats')
get_global_session_stats_parser.set_defaults(func=get_global_session_stats_command)


def get_session_stats_per_user_command():
    print(f"{'USER':<8}  {'MEAN':<8}  {'STD DEV':<8}")
    for user, stats in get_session_stats_per_user(get_log_dicts(args.log_file)).items():
        print(f'{user:<8}  {stats[0]:<8}  {stats[1]:<8}')
    
get_session_stats_per_user_parser = subparsers.add_parser('per-user-stats')
get_session_stats_per_user_parser.set_defaults(func=get_session_stats_per_user_command)


def get_most_and_least_active_users_command():
    least_active, most_active = get_most_and_least_active_users(get_log_dicts(args.log_file))
    print(f'LEAST ACTIVE: {least_active}\nMOST ACTIVE: {most_active}')
    
get_most_and_least_active_users_parser = subparsers.add_parser('most-least-active-users')
get_most_and_least_active_users_parser.set_defaults(func=get_most_and_least_active_users_command)


try:
    args = parser.parse_args()
    args.func()
except:
    print('Something went wrong. Please check your input and try again.')
    exit()