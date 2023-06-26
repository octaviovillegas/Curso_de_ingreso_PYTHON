import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Enunciado:
Debemos mostrar dos números Random  del 1 al 10 y una de las cuatro operaciones básicas (suma, resta y multiplicación) 
para realizar entre estos dos números, estas operaciones también serán Random. En el cuadro de texto resultado el jugador debe 
ingresar el resultado de la operación y presionar el botón  Aceptar.

Luego se debe informar si el resultado es el correcto o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)

        self.label3 = customtkinter.CTkLabel(master=self, text="Resultado")
        self.label3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_respuesta = customtkinter.CTkEntry(master=self, fg_color="green")
        self.txt_respuesta.grid(row=2, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        self.btn_jugar = customtkinter.CTkButton(master=self, text="JUGAR", command=self.btn_jugar_on_click, fg_color="green")
        self.btn_jugar.grid(row=6, pady=30, columnspan=2, rowspan=2,sticky="nsew")


    def deshabilitar_botones(self):
        self.btn_sumar.configure(state="disabled")
        self.btn_restar.configure(state="disabled")
        self.btn_multiplicar.configure(state="disabled")

    def btn_sumar_on_click(self):
        pass

    def btn_restar_on_click(self):
        pass
        
    def btn_multiplicar_on_click(self):
        pass
        
    def btn_jugar_on_click(self):
        self.deshabilitar_botones()
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()