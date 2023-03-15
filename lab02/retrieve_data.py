def retrieve_data() -> str:
    
    data = ""
    
    while True:
        try:
            data += input() + "\n"
        except EOFError:
            break
        
    return data
    

if __name__ == "__main__":
    print(retrieve_data())