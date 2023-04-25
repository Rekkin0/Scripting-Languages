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
        if (not isinstance(length, int) or length <= 0   # type: ignore
            or not isinstance(count, int) or count <= 0  # type: ignore
            or not isinstance(charset, str)):            # type: ignore
            raise SystemExit('Invalid arguments.')
        self.length  = length
        self.count   = count
        self.charset = charset
        self.generated: int = 0
        
    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        import random
        if self.generated == self.count:
            raise StopIteration
        self.generated += 1
        return ''.join(random.choice(self.charset) for _ in range(self.length))
    
    
if __name__ == '__main__':
    pass_gen = PasswordGenerator(length=15, count=6)
    print(next(pass_gen))
    for password in pass_gen:
        print(password)
        
    # bad_pass_gen = PasswordGenerator(length=3.14, count=7.5)
    ...
