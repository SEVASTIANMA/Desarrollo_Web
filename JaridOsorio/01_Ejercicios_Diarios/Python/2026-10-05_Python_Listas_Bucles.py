# ==========================================
# Uso de Listas y Ciclos For en Python
# ==========================================

lenguajes = ["Python", "Dart", "JavaScript", "SQL"]

print("--- LISTA DE TECNOLOGÍAS ---")
for indice, lenguaje in enumerate(lenguajes, start=1):
    print(f"{indice}. {lenguaje}")

# Tabla de multiplicar con ciclo While
print("\n--- Tabla del 3 con While ---")
contador = 1
while contador <= 5:
    print(f"3 x {contador} = {3 * contador}")
    contador += 1