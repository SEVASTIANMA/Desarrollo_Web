# ==========================================
# Manejo de Archivos de Texto y Excepciones en Python
# ==========================================

import os

nombre_archivo = "registro_adso.txt"

def guardar_registro(texto):
    try:
        # Abrir archivo en modo 'append' (añadir al final)
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n")
        print("✅ Registro guardado exitosamente en el archivo.")
    except Exception as e:
        print(f"❌ Ocurrió un error al guardar el archivo: {e}")

def leer_registros():
    if os.path.exists(nombre_archivo):
        print("\n--- CONTENIDO DEL ARCHIVO ---")
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())
    else:
        print("⚠️ El archivo de registro aún no existe.")

# Pruebas de ejecución
guardar_registro("Aprendiz: Jarid - Módulo: Python y Estructuras de Datos")
guardar_registro("Fecha: 11 de Octubre de 2026 - SENA ADSO")

leer_registros()