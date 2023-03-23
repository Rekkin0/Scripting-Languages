from list_tuple_practice import *
from dictionary_practice import *


if __name__ == '__main__':
    
    log = read_log()
    sorted_log = sort_log(log, 6)
    log_by_addr = get_entries_by_addr(log, 'www-b6.proxy.aol.com')
    log_by_code = get_entries_by_code(log, 302)
    log_failed_4xx, log_failed_5xx = get_failed_reads(log)
    log_failed_joined = get_failed_reads(log, True)
    log_by_extension = get_entries_by_extension(log, 'xbm')
    
    # print_entries(log)
    # print_entries(sorted_log)
    # print_entries(log_by_addr)
    # print_entries(log_by_code)  
    # print_entries(log_failed_4xx)
    # print_entries(log_failed_5xx)
    # print_entries(log_failed_joined)
    # print_entries(log_by_extension)
    
    entry_dict = entry_to_dict(log[0])
    # print(entry_dict)
    
    log_dict = log_to_dict(log)
    hosts = get_addrs(log_dict)
    # print(*hosts, sep = '\n')
    # print_dict_entry_dates(log_dict)
