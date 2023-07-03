import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Obtener la hora ingresada en el txt_hora. Al presionar el botón ‘Informar’ 
mostrar mediante alert el mensaje ‘Es de mañana’ 
si la hora ingresada está entre las 7 y las 11
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_hora = customtkinter.CTkLabel(master=self, text="Hora")
        self.label_hora.grid(row=0, column=0, padx=20, pady=10)
        self.txt_hora = customtkinter.CTkEntry(master=self)
        self.txt_hora.grid(row=0, column=1)
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()