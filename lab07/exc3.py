import logging

from exc6 import log


@log(logging.DEBUG)
class PasswordGenerator:
    import string
    def __init__(self, 
                 length: int, 
                 count: int, 
                 charset: str = string.ascii_letters + string.digits,
                 ) -> None:
        self.length  = length
        self.count   = count
        self.charset = charset
        self.generated: int = 0
        
    def __iter__(self) -> 'PasswordGenerator':
        return self
    
    def __next__(self) -> str:
        import random
        if self.generated == self.count:
            raise StopIteration
        self.generated += 1
        return ''.join(random.choice(self.charset) for _ in range(self.length))
    
    
if __name__ == '__main__':
    pass_gen: PasswordGenerator = PasswordGenerator(15, 6)
    print(next(pass_gen))
    for password in pass_gen:
        print(password)
