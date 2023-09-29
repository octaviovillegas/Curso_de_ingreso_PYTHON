# Copyright (C) 2023 <UTN FRA>
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
import customtkinter
import warnings


'''
################# INTRODUCCION #################
#? Un jugador de League of Legends tiene un fin de semana libre y 
#? va a jugar partidas hasta que se canse.
'''
NOMBRE = '' # Completa tu nombre completo solo en esa variable
'''
#?################ ENUNCIADO #################
Para ello deberas programar el boton "Cargar Campeones" para poder cargar 10 personajes del juego.
Para mejorar su jugabilidad, por cada partida jugada va a registrar:
    * Modo de juego ("Normal", "Clasificatoria", "ARAM")
    * Nombre del personaje que usó
    * La cantidad de asesinatos a favor (No puede ser negativo)
    * Muertes en contra (No puede ser negativo)
    * Asistencias a favor. (No puede ser negativo, hasta 40)
    
B)  Al presionar el boton "Mostrar Informe 1" se deberan listar los Campeones
        y su posicion en la lista (por terminal), 
        adicionalmente mostrar el informe del punto C.

#!################ ACLARACION IMPORTANTE #################
Del punto C SOLO debera realizar DOS informes.
Para determinar que informe hacer, tenga en cuenta lo siguiente:

    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)
    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
        Realiza el informe correspondiente al numero obtenido.

EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 
C) Al presionar el boton "Mostrar Informe 2"
    #! 0) - El modo de juego más jugado.
    #! 1) - El modo de juego menos jugado.
    #! 2) - El personaje con el cual murió más.
    #! 3) - El personaje con el cual asistio más.
    #! 4) - El promedio de asesinatos a favor en modo Clasificatoria.
    #! 5) - El promedio de muertes en contra en modo ARAM.
    #! 6) - El promedio de asistencias en modo Normal.
    #! 7) - De la partida con mas muertes en contra, el nombre del personaje y el modo de juego.
    #! 8) - De la partida con mas asistencias a favor, el nombre del personaje y el modo de juego.
    #! 9) - De la partida con mas asesinatos a favor, el nombre del personaje y el modo de juego.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - League of {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"League of {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        
        self.image = tk.PhotoImage(file='./modelos_examenes/league_of_legends_v1/UTN_LoL_App_v1.png')
        self.top_banner = customtkinter.CTkLabel(master = self, image = self.image, text = '')
        self.top_banner.grid_configure(row = 1, column = 0, padx = 20, pady = 5, columnspan = 2, rowspan = 1, sticky = 'we')

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Campeones", command=self.btn_cargar_campeones_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 1", command=self.btn_mostrar_informe_1_on_click)
        self.btn_mostrar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informe 2", command=self.btn_mostrar_informe_2_on_click)
        self.btn_mostrar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Informes", command=self.btn_mostrar_todos_informes_on_click)
        self.btn_mostrar.grid(row=5, pady=10, columnspan=2, sticky="nsew")

        # Datos de prueba para el boton mostrar
        # Cargar aca los pokemones
        self.lista_nombre_campeones = [
            "Jinx", "Akali", "Ashe", "Vladimir", "Kalista",
            "Teemo", "Annie", "Zed", "Katarina", "Hecarim"
        ]
        self.lista_asesinatos_a_favor = [
            9, 7, 7, 4, 12, 20, 5, 7, 14, 15
        ]
        self.lista_asistencias_a_favor = [
            4, 5, 9, 1, 0, 2, 10, 8, 5, 9
        ]

        self.lista_muertes_en_contra = [
            6, 8, 9, 3, 2, 1, 4, 5, 9, 2
        ]

        self.lista_modo_de_juego = [
            "ARAM", "ARAM", "Clasificatoria", "Normal", "Clasificatoria",
            "Clasificatoria", "ARAM", "Clasificatoria", "Normal", "Clasificatoria",
        ]


    def btn_cargar_campeones_on_click(self):
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
