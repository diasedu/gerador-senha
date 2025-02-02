import random
import string

class GeneratePass:
    MIN_LEN = 12

    def __init__(self):
        pass
    
    def generate(self, size: int = None):     
        if size is None:
            size = self.MIN_LEN

        if size < self.MIN_LEN:
            print('O tamanho deve ser maior que 12 caracteres')
            exit()

        charset = string.ascii_letters + string.digits + string.punctuation

        rand_str = ''.join(random.choice(charset) for _ in range(size))

        return rand_str
    
        

        