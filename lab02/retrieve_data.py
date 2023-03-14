def retrieve_data() -> str:
    
    data = ""
    
    for _ in range(1000000):
        try:
            data += input() + "\n"
        except EOFError:
            break
    
    return data