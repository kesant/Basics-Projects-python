# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma(a,b,c):
    resultado=a+b+c
    return resultado
class coche ():
    def __init__(self):
        self.puertas=0
    def aumenta_puertas(self):
        self.puertas+=1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(suma(4,5,6))
    carro=coche()
    carro.aumenta_puertas()
    print(carro.puertas)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
