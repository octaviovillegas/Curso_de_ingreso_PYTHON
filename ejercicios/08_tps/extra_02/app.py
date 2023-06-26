import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
Enunciado:

La UTN nos solicita la creación de una aplicación para obtener información 
estadistica de las evaluaciones.

1. Al presionar el botón "Ingresar notas", se deberá solicitar mediante prompt 
las notas del los alumn@s. 

	A - Se deberá repetir la solicitud hasta que el usuario haga clic en el botón  
    "Cancelar" del prompt
	B - Se deberá validar que la nota sea un numero entero entre el 0 y el 10.
	C - Las notas ingresadas se deberán ir guardando en una lista.

2. Al presionar el botón "Mostrar notas" debemos mostrar por la terminal el 
listado de las notas, primero indicando su posición en la lista y luego el 
valor de la nota. Con el siguiente formato:

        "1 - Nota: 8"
        "2 - Nota: 4"
        "3 - Nota: 10"
        ...

3. Al presionar el botón "Generar Informe" se deberá mostrar mediante alert 
la siguiente información:

	A - Nota mas baja
	B - Nota mas alta
	C - Promedio de todas las notas
	D - Cantidad de evaluaciones con nota 10
	E - En el caso que el promedio sea menor a 3, informar con la leyenda: "El promedio desaprobo"
	En el caso que el promedio sea mayor a 4: "El promedio aprobo"
	En el caso que el promedio sea mayor a 7: "El promedio promocionó"

	Para el punto E se deberá utilizar match.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_ingresar_notas = customtkinter.CTkButton(master=self, text="Ingresar Notas", command=self.btn_ingresar_notas_on_click)
        self.btn_ingresar_notas.grid(row=3, pady=20, columnspan=2, sticky="news")

        self.btn_mostrar_notas = customtkinter.CTkButton(master=self, text="Mostrar Notas", command=self.btn_mostrar_notas_on_click)
        self.btn_mostrar_notas.grid(row=4, pady=20, columnspan=2, sticky="news")
        
        self.btn_generar_informe_notas = customtkinter.CTkButton(master=self, text="Generar Informe de Notas", command=self.btn_generar_informe_notas_on_click)
        self.btn_generar_informe_notas.grid(row=5, pady=20, columnspan=2, sticky="news")
        
            
    def btn_ingresar_notas_on_click(self):
        pass
        
    
    def btn_generar_informe_notas_on_click(self):
        pass
        
    def btn_mostrar_notas_on_click(self):
        pass
            