import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from datetime import time
import customtkinter


'''
Luego de presionar el botón 'Iniciar',se disparara un temporizador de 2s que haga visible el botón oculto.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_oculto = customtkinter.CTkButton(master=self, text="Boton Oculto", command=None)
        #self.btn_oculto.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        #self.btn_oculto.grid_forget()
 
    def btn_mostrar_on_click(self):
        pass

    def activar_boton_oculto(self):
        pass
        

if __name__ == "__main__":
    app = App()
    app.mainloop()