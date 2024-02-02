import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_07
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad - Validar (Entre 15 y 90 años).
    Genero - Validar (Femenino/Masculino/No Binario).
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los masculinos.
    B. Porcentaje de femeninos mayores de 18 respecto al total de personas.
    C. Porcentaje de personas de cada genero.
    D. Informar edad y genero de la persona con menor edad, puede ser mas de una.
    E. Cuál fue el genero mas ingresado.

Nota: Se podrán hacer como máximo 10 ingresos.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label = customtkinter.CTkLabel(master=self, text="Edad")
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Genero")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_genero = customtkinter.CTkEntry(master=self)
        self.txt_genero.grid(row=1, column=1)

        self.btn_ingresar = customtkinter.CTkButton(master=self, text="INGRESAR", command=self.btn_ingresar_on_click)
        self.btn_ingresar.grid(row=2, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_mostrar_a = customtkinter.CTkButton(master=self, text="MOSTRAR A", command=self.btn_mostrar_a_on_click)
        self.btn_mostrar_a.grid(row=3, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_mostrar_b = customtkinter.CTkButton(master=self, text="MOSTRAR B", command=self.btn_mostrar_b_on_click)
        self.btn_mostrar_b.grid(row=4, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_mostrar_c = customtkinter.CTkButton(master=self, text="MOSTRAR C", command=self.btn_mostrar_c_on_click)
        self.btn_mostrar_c.grid(row=5, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_mostrar_d = customtkinter.CTkButton(master=self, text="MOSTRAR D", command=self.btn_mostrar_d_on_click)
        self.btn_mostrar_d.grid(row=6, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_mostrar_e = customtkinter.CTkButton(master=self, text="MOSTRAR E", command=self.btn_mostrar_e_on_click)
        self.btn_mostrar_e.grid(row=7, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.lista_edades = []
        self.lista_generos = []


    def btn_ingresar_on_click(self):
        pass

    def btn_mostrar_a_on_click(self):
        pass

    def btn_mostrar_b_on_click(self):
        pass
    
    def btn_mostrar_c_on_click(self):
        pass

    def btn_mostrar_d_on_click(self):
        pass

    def btn_mostrar_e_on_click(self):
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x400")
    app.mainloop()