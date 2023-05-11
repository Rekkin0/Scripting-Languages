from log_entries.AcceptedPasswordSSHLogEntry import AcceptedPasswordSSHLogEntry
from log_entries.FailedPasswordSSHLogEntry import FailedPasswordSSHLogEntry
from log_entries.ErrorSSHLogEntry import ErrorSSHLogEntry
from log_entries.OtherSSHLogEntry import OtherSSHLogEntry
from SSHLogJournal import SSHLogJournal
from SSHUser import SSHUser


if __name__ == '__main__':
    journal = SSHLogJournal()
    
    log1 = 'Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2'
    log2 = 'Dec 10 09:31:24 LabSZ sshd[24676]: Failed password for invalid user FILTER from 104.192.3.34 port 33738 ssh2'
    log3 = 'Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]'
    log4 = 'Dec 10 11:03:45 LabSZ sshd[25459]: pam_unix(sshd:auth): check pass; user unknown'
    
    journal.append(log1); journal.append(log2)
    journal.append(log3); journal.append(log4)
    
    entry1, entry2 = journal.get_entry(0), journal.get_entry(1)
    entry3, entry4 = journal.get_entry(2), journal.get_entry(3)
    
    print(entry2)
    print('has ip:\t', entry2.has_ipv4, entry2.get_ipv4())
    print(entry4)
    print('no ip:\t', entry4.has_ipv4, entry4.get_ipv4())
    print()
    
    print(entry1)
    print('validate:\t', entry1.validate())
    wrong_entry = AcceptedPasswordSSHLogEntry('Dec 10 09:31:24 LabSZ sshd[24676]: Failed password for invalid user FILTER from 104.192.3.34 port 33738 ssh2')
    print(wrong_entry)
    print('validate:\t', wrong_entry.validate())
    print()
    
    print('[1]', entry1)
    print('[2]', entry2)
    print('2 > 1:\t', entry2 > entry1)
    print('[3]', entry3)
    print('1 < 3:\t', entry1 < entry3)
    print('1 == 2:\t', entry1 == entry2)
    print('3 == 3:\t', entry3 == entry3)
    print()
    
    # zad 7
    # can be iterated
    print('entries in journal (iterable):')
    for entry in journal:
        print(entry)
    print('journal len:\t', len(journal))
    print()
    print(entry1)
    print('in journal:\t', entry1 in journal)
    print(wrong_entry)
    print('in journal:\t', wrong_entry in journal)
    print()
    
    print('get entries by ipv4 (119.137.62.142):\t', journal.get_entries_by_ipv4('119.137.62.142'))
    print()
    print('get entries in time range (from 10 to 11 Dec (exclusive)):\t', end='')
    print(journal.get_entries_in_time_range('10/12', '11/12')) # date format: dd/mm
    print()
    
    # zad 8
    user1 = SSHUser("fztu", "10/12/2020 09:32:20") # date format: dd/mm/yyyy hh:mm:ss
    print('user1', user1)
    user2 = SSHUser("^*&%(@#)", "10/12/2020 09:32:20")
    print('user2', user2)
    
    all_list = [entry1, entry2, entry3, entry4, user1, user2]
    print('validate all (exc8):\t')
    [print(entry, ':', entry.validate()) for entry in all_list]
    print()
    
    not_a_log = 'ghrkjeklgsbvcadelrhblf'
    print('can append to journal:', not_a_log)
    journal.append(not_a_log)
