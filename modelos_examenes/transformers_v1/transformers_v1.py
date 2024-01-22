# Copyright (C) 2024 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import warnings

import customtkinter

'''
################# INTRODUCCION #################
#? En Cybertron se requiere contabilizar los transformers que hay en guerra 
#? para ello habra que construir un programita que ayude con esa cuestion y 
#? recobrar la paz.
'''
NOMBRE = '' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
Es por eso que deberas programar el boton "Cargar Transformer" para poder cargar 10 robots.
Los datos que deberas pedir para los transformers son:
    * El nombre del transformer
    * El bando del transformer (Autobot, Maximal, Predacon, Descepticon, Terrorcon)
    * La cantidad de poder (validar que sea mayor a 50 y menor a 200)
    * La altura (en metros enteros [sin decimales]) del transformer (Validar que sea mayor a 5 y menor a 50)
    * El peso (en toneladas) del transformer (Validar que sea mayor a 20 y menor a 500)

B) Al presionar el boton "Mostrar Informe 1" se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - Cantidad de Transformers del bando Autobots
    #! 1) - Cantidad de Transformers del bando Maximals
    #! 2) - Nombre, bando, poder, altura y peso del Transformer con el poder mas alto
    #! 3) - Nombre, bando, poder, altura y peso del Transformer con el peso mas bajo
    #! 4) - Cantidad de Transformers, con mas de 150 de poder.
    #! 5) - Cantidad de Transformers, con menos de 25 metros de altura
    #! 6) - Bando de los Transformers del bando que mas Transformers posea 
    #! 7) - Bando de los Transformers del Bando que menos Transformers posea 
    #! 8) - el promedio de poder de todos los Transformers ingresados
    #! 9) - el promedio de poder de todos los Transformers del bando Descepticon
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Cybertron Manager de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Cybertron Manager de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/transformers_v1/UTN_Transformers_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Transformers", command=self.btn_cargar_transformer_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Ambos Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para boton mostrar
        # Cargar aca los transformers
        self.lista_nombre_transformers = [
            "OptimusPrime", "OptimusPrimal", "Megatron", "Airazor", "Cheetor",
            "Wheeljack", "Starscream", "Bumblebee", "Mirage", "Scourge", "Megatron"
        ]
        self.lista_poder_transformers = [
            200, 199, 198, 140, 150,
            130, 120, 145, 125, 199, 190
        ]
        self.lista_bando_transformers = [
            "Autobot", "Maximal", "Descepticon", "Maximal", "Maximal",
            "Autobot", "Descepticon", "Autobot", "Autobot", "Terrorcon", "Predacon"
        ]
        self.lista_altura_transformers = [
            30, 25, 35, 20, 22,
            20, 16, 12, 15, 40, 34
        ]
        self.lista_peso_transformers = [
            300, 390, 450, 250, 175,
            200, 180, 105, 90, 350, 420
        ]


    def btn_cargar_transformer_on_click(self):
        pass
        

    def btn_mostrar_informe_1_on_click(self):
        pass

    
    def btn_mostrar_informe_2_on_click(self):
        pass

    
    def btn_mostrar_todos_informes_on_click(self):
        self.btn_mostrar_informe_1_on_click()
        self.btn_mostrar_informe_2_on_click()

            

    
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()