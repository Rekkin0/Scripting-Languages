from retrieve_data import retrieve_data
from lab_3_a import reduce_request


if __name__ == '__main__':
    
    data = retrieve_data().splitlines(True)
    print(reduce_request(data, "404"))