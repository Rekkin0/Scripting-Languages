from utils import retrieve_data, process_data
from lab_3_a import reduce_request


if __name__ == '__main__':
    
    raw_data = retrieve_data().splitlines(True)
    data = process_data(raw_data)
    print(reduce_request(data, "302"))