import sqlite3

#Abrir o crear una conexion

miConexion = sqlite3.connect("Primerabase.db")

#Creamos un cursor

miCursor = miConexion.cursor()

#Creamos nuestra primera tabla

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")

#Insertar datos en las tablas

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")


#----------------Segunda Parte del Tuturial Base de Datos Agregar varios articulos a la base de datos--------------------------------------

""" variosProductos=[
    ("Camiseta",10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Peluche",20,"Jugueteria")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos) """

#---------------lEER INFORMACION DE LA BASE DE DATOS--------------------

miCursor.execute("SELECT * FROM PRODUCTOS")

ProductosVarios = miCursor.fetchall()

print(ProductosVarios)



#Verificar Cambios

miConexion.commit()







#cerrar la conexion

miConexion.close()

