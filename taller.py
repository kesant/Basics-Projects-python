


ldatos = ['JUAN PEREZ|QUITO|1200', 'MARIA RICAURTE|LOJA|2300', 'RENE RIVAS|IBARRA|1000', 'RICARDO LEON|CUENCA|1500',
 'PEDRO CIFUENTES|MANTA|1899', 'JUAN ARBOLEDA|QUITO|2229', 'LUISA HERRERA|LOJA|2010', 'PATRICIO SOSA|IBARRA|750',
  'EDUARDO MALO|CUENCA|900', 'ROCIO LARREA|MANTA|1011', 'CATALINA GUERRA|QUITO|1045', 'FERNANDO ORTIZ|LOJA|1023', 
  'MARIO GUERRON|IBARRA|1034', 'ANA LLERENA|CUENCA|1056', 'PABLO PITARQUE|MANTA|1035', 'DOLORES RIBADENEIRA|MANTA|1066',
   'PETER VILLEGAS|QUITO|1087', 'JUAN SALAS|CUENCA|1095', 'MARIA SOL GALARZA|LOJA|2345', 'MARISOL RESTREPO|QUITO|3021']

def CargarInformacion(lnomina) :
    list_nom=[]
    list_ciudad=[]
    list_sueldo=[]
    for dato in lnomina:
        nombre,ciudad,sueldo=dato.split("|")
        list_nom.append(nombre)
        list_ciudad.append(ciudad)
        list_sueldo.append(int(sueldo))
    return list_nom,list_ciudad,list_sueldo



def EncontrarSueldoLimite(lnombres, lsueldos, busqueda = True):
    if busqueda==True:
        valor=max(lsueldos)
        nombre=lnombres[lsueldos.index(valor)]
        print(f" La persona con mayor sueldo es {nombre} con sueldo de : {valor}")
    else:
        valor=min(lsueldos)
        nombre=lnombres[lsueldos.index(valor)]
        print(f" La persona con menor sueldo es {nombre} con sueldo de : {valor}")


######################main#############################
menu ="""
Opción 1: Mostrar el nombre del empleado con el sueldo más bajo y con el sueldo más alto de toda la nomina

Opción 2: El nombre del empleado con el sueldo más bajo y con el sueldo más alto en una ciudad ingresada por el usuario
"""
print(menu)
validador=True
while validador :
    opcion=input("ingrese el numero de la opcion :")
    if opcion =="2" or opcion=="1":
        validador=False
    else:
        print("ingreso una opcion invalida")
lista_nom,lista_ciudad,lista_sueldo=CargarInformacion(ldatos)
if opcion=="1":
    EncontrarSueldoLimite(lista_nom, lista_sueldo,False)
    EncontrarSueldoLimite(lista_nom, lista_sueldo,True)
if opcion=="2":
    validador=0
    nueva_nombre=[]
    nueva_sueldo=[]
    while validador==0:
        ciudad=input("Ingrese una ciudad :").upper()
        for indice in range(len(lista_ciudad)):
            if ciudad==lista_ciudad[indice]:
                nueva_nombre.append(lista_nom[indice])
                nueva_sueldo.append(lista_sueldo[indice])
                print(nueva_nombre)
                validador+=1
        if validador==0:
            print("ingresaste una ciudad invalida , vuelve ingresar la ciudad ")    
    EncontrarSueldoLimite(nueva_nombre, nueva_sueldo,False)
    EncontrarSueldoLimite(nueva_nombre, nueva_sueldo,True)
