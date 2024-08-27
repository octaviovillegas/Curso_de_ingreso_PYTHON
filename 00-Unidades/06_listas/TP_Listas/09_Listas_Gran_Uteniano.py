import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: Gran_uteniano
---
Enunciado:
INTRODUCCION:
Es la gala de eliminación del Gran Utniano y la producción nos pide un programa para contar los votos de 
los televidentes y saber cuál será el participante que deberá abandonar la casa más famosa del mundo.
Los participantes en la placa son: Giovanni, Gianni y Facundo. Fausto no fue nominado y Marina no está 
en la placa esta semana por haber ganado la inmunidad.

ENUNCIADO:
Cada televidente que vota deberá ingresar:
* Nombre del votante
* Edad del votante (debe ser mayor a 13)
* Género del votante (Masculino, Femenino, Otro)
* El nombre del participante a quien le dará el voto negativo (Debe estar en placa)

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario mediante alert:
    A) El promedio de edad de las votantes de género Femenino 
    B) Cantidad de personas de género masculino entre 25 y 40 años que votaron a Giovanni o a Facundo.
    C) Nombre del votante más joven qué votó a Gianni.
    D) Nombre de cada participante y porcentaje de los votos qué recibió.
    E) El nombre del participante que debe dejar la casa (El que tiene más votos)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Gran UTENIANO")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba
        # Cargar o modificar datos en estas listas
        self.lista_nombres = ["Pepe", "Moni","Paola","Coki", "Dardo", "Maria", "Fatiga"]
        self.lista_edades = [55, 45, 18, 17, 49, 45, 14]
        self.lista_genero = ["Masculino", "Femenino", "Femenino", "Masculino", "Masculino", "Femenino", "Otro"] 
        self.lista_participantes = ["Giovanni", "Gianni", "Facundo", "Gianni", "Gianni", "Facundo", "Giovanni"]


    def btn_mostrar_on_click(self):
        pass

    def btn_cargar_on_click(self):
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()