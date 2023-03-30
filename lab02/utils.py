import re
from typing import List, Match


def retrieve_data() -> str:
    data = ""
    while True:
        try:
            data += input() + "\n"
        except EOFError:
            break
        
    return data


REGEX = re.compile(r"(.+) - - \[(.+)\] \"(.+)\" (.+) (.+)")
def process_line(raw_line: str) -> Match[str]:
    line = REGEX.match(raw_line)
    if line is None:
        raise Exception(f"Invalid line: {raw_line}")
    
    return line


def process_data(raw_data: List[str]) -> List[Match[str]]:
    data = []
    for line in raw_data:
        try:
            data.append(process_line(line))
        except Exception as e:
            # print(e)
            continue
    
    return data


def get_host(line: Match[str]) -> str:
    return line.group(1)


def get_timestamp(line: Match[str]) -> str:
    return line.group(2).split()[0]


def get_request(line: Match[str]) -> str:
    return line.group(3)


def get_resource_path(line: Match[str]) -> str:
    request = get_request(line).split()
    return (request[1] if len(request) > 1 else request[0]).strip()
    

def get_status_code(line: Match[str]) -> str:
    return line.group(4)


def get_resource_size(line: Match[str]) -> str:
    return line.group(5)
 

if __name__ == "__main__":
    print(retrieve_data())