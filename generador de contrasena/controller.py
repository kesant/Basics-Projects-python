
from model import PasswordModel
from utility import *

class PasswordController:
    
    def __init__(self):
        self.__obj = PasswordModel()

    def process_password(self, strength):
        if strength == EASY:
            self.__obj.generate(LENGTH_S)
        elif strength == MEDIUM:
            self.__obj.generate(LENGTH_M)
        elif strength == HARD:
            self.__obj.generate(LENGTH_L)
        else:
            self.__obj.generate(LENGTH_XL)

        return self.__obj.get_password()
                            