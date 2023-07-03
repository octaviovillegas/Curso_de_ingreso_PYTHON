import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Luego de presionar el botón 'Iniciar', se debe disparar, 3 segundos después, un saludo con el mensaje "Bienvenido a la UTN FRA".

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.contador  = 0

    def btn_mostrar_on_click(self):
        pass

    def mostrar_mensaje(self):
        pass
        
            

if __name__ == "__main__":
    app = App()
    app.mainloop()