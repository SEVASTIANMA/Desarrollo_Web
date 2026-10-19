# ==========================================
# Manejo de Tuplas y Conjuntos (Sets) en Python
# ==========================================

# 1. Tuplas (Estructuras inmutables)
coordenadas_sena = (10.96854, -74.78132)  # Latitud y Longitud
print("--- COORDENADAS (TUPLA) ---")
print(f"Latitud: {coordenadas_sena[0]}, Longitud: {coordenadas_sena[1]}")

# 2. Conjuntos / Sets (Elementos únicos sin duplicados)
lenguajes_aprendiz = {"Python", "Dart", "SQL", "Python", "VBA"}
print("\n--- TECNOLOGÍAS ÚNICAS (SET) ---")
print(lenguajes_aprendiz)  # Python no se repetirá

# Agregar un nuevo lenguaje
lenguajes_aprendiz.add("JavaScript")
print(f"Lista actualizada: {lenguajes_aprendiz}")