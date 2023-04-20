import string


class PasswordGenerator:
    def __init__(
            self, 
            length: int, 
            count: int, 
            charset = string.ascii_letters + string.digits
        ) -> None:
        self.length = length
        self.count = count
        self.charset = charset
        
    def __iter__(self) -> 'PasswordGenerator':
        return self
    
    def __next__(self) -> str:
        import random
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        return ''.join(random.choice(self.charset) for _ in range(self.length))