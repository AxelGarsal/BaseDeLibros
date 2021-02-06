import sqlite3
conexion=sqlite3.connect("Biblioteca")
#con el cursor de crean las tablas y ejecuta los querry
cursor=conexion.cursor()
#creamos la la tabla y sus atributos con los adecuados tipos de datos
#Una vez creadas las tablas es necesario comentarlas para no tener errores

cursor.execute("CREATE TABLE LIBRO (TITULO VARCHAR(50), "
               "AUTOR VARCHAR(20), ID INTEGER, ISBN INTEGER )")

cursor.execute("CREATE TABLE INFO (EDICION VARCHAR(15),"
               "EDITORIAL VARCHAR (25), PAGINAS INTEGER, AÑO DATE)")

cursor.execute("CREATE TABLE UBICACION (SALA VARCHAR (20), NIVEL INTEGER )")



#conexion.commit()

conexion.close()
