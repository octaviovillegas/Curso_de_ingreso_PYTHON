import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import time
import customtkinter


'''
8 - Luego de presionar el botón 'Iniciar',se disparara ; un temporizador de una función que haga visible el botón "el oculto". 
Al pulsar el botón "el oculto" se deberá calcular la cantidad de segundos transcurridos desde que este se comenzó a visualizar hasta que fue pulsado.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=1, pady=10, columnspan=2, sticky="nsew")

        self.btn_oculto = customtkinter.CTkButton(master=self, text="Boton Oculto", command=self.btn_oculto_on_click)
        #self.btn_oculto.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        #self.btn_oculto.grid_forget()
 
    def btn_mostrar_on_click(self):
        pass
        
    
    def btn_oculto_on_click(self):
        pass
        

    def activar_boton_oculto(self):
        pass
        

if __name__ == "__main__":
    app = App()
    app.mainloop()