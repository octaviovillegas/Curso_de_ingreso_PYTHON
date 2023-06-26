import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo  coctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar 
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio




'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_nombre_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_nombre_articulo = ['TV','LICUADORA']
        self.lista_precio_articulo = [1000,200]


    def btn_agregar_on_click(self):
        
        nombre_articulo = self.txt_nombre_articulo.get()
        if(len(nombre_articulo) != 0):
            flag_nombre_articulo_ok = True

        precio_articulo_texto = self.txt_precio_articulo.get() 
        if(len(precio_articulo_texto) != 0):   
            flag_precio_articulo_ok = True
        
        for letra in nombre_articulo:
            if(letra < "A" or letra > "Z"):
                flag_nombre_articulo_ok = False
                alert(title="ERROR",message="El nombre debe solo contener caracteres de la A a la Z")
                break

        for letra in precio_articulo_texto:
            if(letra < "0" or letra > "9"):
                flag_precio_articulo_ok = False
                alert(title="ERROR",message="El precio debe solo contener caracteres de la 0 al 9")
                break

        if(flag_nombre_articulo_ok == True and flag_precio_articulo_ok == True):
            self.lista_nombre_articulo.append(nombre_articulo)
            self.lista_precio_articulo.append(int(precio_articulo_texto))
            alert(title="EXITO",message="La carga fue exitosa")
    


    def btn_mostrar_on_click(self):
        cantida_elementos = len(self.lista_nombre_articulo)
        for indice in range(cantida_elementos):
            mensaje = "Indice: {0} - {1} - {2}".format(indice,self.lista_nombre_articulo[indice], self.lista_precio_articulo[indice])
            print(mensaje)


    def btn_informar_on_click(self):
       pass


if __name__ == "__main__":
    app = App()
    app.mainloop()    