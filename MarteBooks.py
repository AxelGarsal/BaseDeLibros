from tkinter import *
from tkinter import messagebox
import sqlite3

conexion=sqlite3.connect("Biblioteca")
#con el cursor de crean las tablas y ejecuta los querry
cursor=conexion.cursor()
#creamos la la tabla y sus atributos con los adecuados tipos de datos
#Una vez creadas las tablas es necesario comentarlas para no tener errores

#cursor.execute("CREATE TABLE LIBRO (TITULO VARCHAR(50), "
               #"AUTOR VARCHAR(20), ID INTEGER, ISBN INTEGER )")

#cursor.execute("CREATE TABLE INFO (EDICION VARCHAR(15),"
               #"EDITORIAL VARCHAR (25), PAGINAS INTEGER, AÑO DATE)")

#cursor.execute("CREATE TABLE UBICACION (SALA VARCHAR (20), NIVEL INTEGER )")
#conexion.commit()
conexion.close()

# P A R A  L O  G R A F I C O
raiz = Tk()
#la barra que tendra las opciones del menú
barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width='300', height='300')
#primera opcion
basePrincipal = Menu(barraMenu, tearoff=0)
basePrincipal.add_command(label='Conectar')
basePrincipal.add_command(label='Salir')
#opcion para borrar todos los campos
borrarPrincipal = Menu(barraMenu, tearoff=0)
borrarPrincipal.add_command(label='Borrar campos')
#para el abc o crud
abcPrincipal = Menu(barraMenu, tearoff=0)
abcPrincipal.add_command(label='Agregar')
abcPrincipal.add_command(label='Leer')
abcPrincipal.add_command(label='Actualizar')
abcPrincipal.add_command(label='Borrar')
#otra
ayudaPrincipal = Menu(barraMenu, tearoff=0)
ayudaPrincipal.add_command(label='ayuda')
ayudaPrincipal.add_command(label='creador')
#ahora agregamos con el metodo cascada las opciones a la barra del menu
barraMenu.add_cascade(label='BBDD', menu=basePrincipal)
barraMenu.add_cascade(label='BORRAR', menu=borrarPrincipal)
barraMenu.add_cascade(label='CRUD', menu=abcPrincipal)
barraMenu.add_cascade(label='AIUDA', menu=ayudaPrincipal)


raiz.mainloop()


