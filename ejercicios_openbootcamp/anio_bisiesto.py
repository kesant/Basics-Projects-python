usuario=int(input("ingrese el anio : "))
modo=False

if usuario%4==0:
    if usuario%100==0:
        if usuario%400==0:
            modo=True
    else:
        modo=True

if modo:
    print(f"el anio {usuario} es bisiesto")
else:
    print(f"el anio {usuario} no es bisiesto")