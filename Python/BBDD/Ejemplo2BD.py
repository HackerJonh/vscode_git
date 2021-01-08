import sqlite3

conexion = sqlite3.connect("GestionProductos.db")

miCursor = conexion.cursor()

miCursor.execute('''
    
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

Productos = [
    ("AR01", "Pelota", 20, "Jugueteria"),
    ("AR02", "Pantalon", 15, "Confeccion"),
    ("AR03", "Destornillador", 25, "Ferreteria"),
    ("AR04","Jarron",45,"Ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?,?)",Productos)







conexion.commit()
conexion.close()