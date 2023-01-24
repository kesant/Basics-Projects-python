  
from entity import Password
from random import randint, choice
from utility import *

class PasswordModel:
    def __init__(self):
        self.__obj = Password()
        self.__password = None

    def generate(self, length):
        self.__password = []
        
        for i in range(length):
            char_type = randint(1, 100)
            
            if char_type <= LETTER:
                char = choice(self.__obj.characters)
            elif char_type <= PUNCTUATION:
                char = choice(self.__obj.digits)
            else:
                char = choice(self.__obj.punctuation)

            self.__password.append(char)
    
    def get_password(self):
        return ''.join(self.__password)
