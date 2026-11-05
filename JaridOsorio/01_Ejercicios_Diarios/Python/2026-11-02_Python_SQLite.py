# ==========================================
# Introducción a Bases de Datos con SQLite en Python
# ==========================================

import sqlite3

def gestionar_base_datos():
    # Conectar a una base de datos local (se crea automáticamente si no existe)
    conexion = sqlite3.connect("sena_adso.db")
    cursor = conexion.cursor()

    # Crear una tabla de aprendices
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aprendices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ficha TEXT NOT NULL
        )
    """)

    # Insertar un registro de prueba
    cursor.execute("INSERT INTO aprendices (nombre, ficha) VALUES (?, ?)", ("Jarid Osorio", "3532730"))
    conexion.commit()

    # Consultar los registros
    cursor.execute("SELECT * FROM aprendices")
    registros = cursor.fetchall()
    
    print("--- REGISTROS EN LA BASE DE DATOS ---")
    for reg in registros:
        print(reg)

    conexion.close()

gestionar_base_datos()
