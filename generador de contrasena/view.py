import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from controller import *
import tkinter.messagebox

class Aplication:
    def __init__(self):
        self.window = tk.Tk() #self.window sera la ventana que estamos viendo
        self.obj = PasswordController()# objeto o instancia de pasword controller
        self.random_password = tk.StringVar() #creamos una variable de tipo string que almacenara la contrasena para gurardarla
        self.selected = tk.StringVar()#creamos una variable que se encarga de guardar la seleccion del grado de dificultad de la contrasena
        self.labelvar = tk.StringVar()#Esta variable nos ayudara a guardar el mensaje de "copiado a portapapeles"

        #WINDOWS SETTINGS
        self.window.title("PASSWORD GENERATOR")#Nombre de la ventana
        self.window.geometry("550x340+675+300") #dimensiones y posiciones de la ventana en la pantalla (X, Y)
        self.window.resizable(0, 0) #Hacemos que el tamano de la pantalla sea fijo e inalterable 
        self.window.iconbitmap("./imagenes/lock.ico") #el icono de la ventana

        #DRAW A LINE
        self.canvas = Canvas(self.window, width = 520, height = 30)#creamos un canvas para empezar a dibujar sobre el
        self.canvas.place(x = 15, y = 35)#posicionamos el canvas en la parte que queremos en la ventana
        self.canvas.create_line(0, 25, 520, 25, fill = 'black')#dibujamos una linea de color negro que parte de 0 a 520 en X y 25 en Y

        #CREATE A STANDARD STYLE FOR TITLES
        self.t_style = ttk.Style()#inicializamos una variable para asignarle una configuraciion de estilo
        self.t_style.configure("BW.TLabel", foreground="black", font=("Helvetica", 24))#especificamos el estilo de esa variable
        #CREATE A STANDARD STYLE FOR SUBTITLES
        self.s_style = ttk.Style()#inicializamos una variable para asignarle una configuraciion de estilo
        self.s_style.configure("WB.TLabel", foreground="black", font=("Helvetica", 14))#especificamos el estilo de esa variable
        #SPECIAL STYLE
        self.sp_style = ttk.Style()#inicializamos una variable para asignarle una configuraciion de estilo
        self.sp_style.configure("GB.TLabel", foreground="green", font=("Helvetica", 16))#especificamos el estilo de esa variable
        
        #TEXT LABELS
        self.label1 = ttk.Label(self.window, text="Password Generator", style="BW.TLabel").place(x = 140, y = 10)#creamos y ubicamos el texto
        self.label2 = ttk.Label(self.window, text="Length:", style="WB.TLabel").place(x = 20, y = 80)#creamos y ubicamos el texto
        #creamos y ubicamos el texto pero le se asigna la variable creada en la linea 13 para mostrarla y ocultarla
        self.label3 = ttk.Label(self.window, textvariable=self.labelvar, style="GB.TLabel").place(x = 350, y = 260)

        #RADIO BUTTONS
        self.rdbtn1 = ttk.Radiobutton(self.window, text="Short", variable=self.selected, value="0").place(x = 100, y = 120)
        self.rdbtn2 = ttk.Radiobutton(self.window, text="Medium", variable=self.selected, value="1").place(x = 185, y = 120)
        self.rdbtn3 = ttk.Radiobutton(self.window, text="Large", variable=self.selected, value="2").place(x = 285, y = 120)
        self.rdbtn4 = ttk.Radiobutton(self.window, text="Extra Large", variable=self.selected, value="3").place(x = 370, y = 120)

        #TEXTBOX
        self.txtbox = ttk.Entry(self.window, textvariable = self.random_password, state = "disable", justify = "center", font = ("Argentum Sans", 24)).place(x = 90, y = 180)

        #BUTTONS -> generate FUNCTION & copy FUNCTION
        self.btn1 = ttk.Button(text = "Copy", command = self.copy).place(x = 237, y = 240)
        self.btn2 = ttk.Button(text = "Generate", command = self.generate).place(x = 237, y = 280)

        self.window.mainloop()

    def generate(self):
        try:
            self.labelvar.set("")
            self.random_password.set("")
            value = int(self.selected.get())
            self.random_password.set(self.obj.process_password(value))
        except:
            tkinter.messagebox.showwarning("Error", "Select a length")

    def copy(self):
        if self.random_password.get() != "":
            self.window.clipboard_clear()
            self.window.clipboard_append(self.random_password.get())
            self.labelvar.set("Copied!")
        else:
            tkinter.messagebox.showwarning("Error", "Generate a password first")

if __name__ == "__main__": 
    Aplication = Aplication()
