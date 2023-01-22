class Alumno:
    def __init__(self,nombre,nota) :
        self.nombre=nombre
        self.nota=nota
        self.status="no conocido"
    def informacion(self):
        
        print(f"""
        Nombre : {self.nombre} 
        Nota :{self.nota}
        Status: {self.status}
        """)
    def status(self,nota):
        if nota >7 :
            self.status="Aprobado"
        else:
            self.status="Reprobado"

if __name__=="__main__":
    estudiante =Alumno("Kevin",8.56)
    estudiante.informacion()