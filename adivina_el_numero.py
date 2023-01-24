import random
def run():
    numero_aleatorio=random.randint(1,100)
    numero_elegido=int(input("ingrese un numero :"))
    while numero_aleatorio!=numero_elegido:
        if numero_aleatorio<numero_elegido:
            print("elige un numero mas pequeño")
        else:
             print("elige un numero mas grande")
        numero_elegido=int(input("ingrese otro numero :"))        
    print("Ganaste!!")         

if __name__=="__main__":
    run()