from utils import Data, get_status_code


def reduce_request(data: Data, status_code: int) -> int:
    return sum(1 for line in data if get_status_code(line) == status_code)