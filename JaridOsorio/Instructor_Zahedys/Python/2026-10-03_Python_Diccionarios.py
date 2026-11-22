# ==========================================
# Uso de Diccionarios en Python (Clave-Valor)
# ==========================================

# Creación de un diccionario para almacenar información de un estudiante ADSO
estudiante_adso = {
    "nombre": "Jarid",
    "ficha": "3532730",
    "programa": "Análisis y Desarrollo de Software",
    "trimestre": 2,
    "activo": True
}

print("--- INFORMACIÓN DEL APRENDIZ ---")
print(f"Nombre: {estudiante_adso['nombre']}")
print(f"Programa: {estudiante_adso['programa']}")
print(f"Ficha: {estudiante_adso['ficha']}")

# Modificar y agregar un nuevo campo
estudiante_adso["promedio"] = 4.7
print(f"\nPromedio actualizado: {estudiante_adso['promedio']}")