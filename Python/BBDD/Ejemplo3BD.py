import sqlite3

miConexion = sqlite3.connect("GestionProducto2.db")

miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR (20))
''')

productos=[
    ("Pelota",20,"Jugueteria"),
    ("Pantalon",25,"Confeccion"),
    ("Destornillador",30,"Ferreteria"),
    ("Jarron",25,"Ceramica")

    ]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

miConexion.commit()
miConexion.close()
