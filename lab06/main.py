from SSHLogEntryAcceptedPassword import SSHLogEntryAcceptedPassword
from SSHLogEntryFailedPassword import SSHLogEntryFailedPassword
from SSHLogEntryError import SSHLogEntryError
from SSHLogEntryOther import SSHLogEntryOther
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
    
    print(entry1)
    print('has ip:\t', entry2.has_ipv4, entry2.get_ipv4())
    print('no ip:\t', entry4.has_ipv4, entry4.get_ipv4())
    
    wrong_entry = SSHLogEntryAcceptedPassword('Dec 10 09:31:24 LabSZ sshd[24676]: Failed password for invalid user FILTER from 104.192.3.34 port 33738 ssh2')
    print('validate:\t', entry1.validate(), wrong_entry.validate())
    
    print('__gt__, __lt__:\t', entry4 > entry3, entry1 < entry2)
    print('__eq__:\t', entry2 == entry3, entry1 == entry1)
    
    #can be iterated
    for entry in journal:
        pass
    
    print('__len__:\t', len(journal))
    print('__contains__:\t', entry1 in journal, wrong_entry in journal)
    
    print('get_entries_by_ipv4:\t', journal.get_entries_by_ipv4('119.137.62.142'))
    print('get_entries_in_time_range:\t', journal.get_entries_in_time_range('9/12', '10/12')) # date format: dd/mm
    
    user1 = SSHUser("fztu", "10/12/2020 09:32:20") # date format: dd/mm/yyyy hh:mm:ss
    user2 = SSHUser("^*&%(@#)", "10/12/2020 09:32:20")
    
    all_list = [entry1, entry2, entry3, entry4, user1, user2]
    print('validate all:\t', end='')
    [print(entry.validate(), end=' ') for entry in all_list]