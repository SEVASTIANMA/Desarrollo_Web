# 1. Definimos la lista inicial de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista auxiliar donde guardaremos únicamente las asignaturas que se deben repetir
para_repetir = []

# 2. Recorremos cada asignatura para pedir la nota
for asignatura in asignaturas:
    # Solicitamos la nota al usuario en el rango de 0 a 100
    nota = float(input(f"¿Qué nota sacaste en {asignatura}? (0-100): ")) 
    #si superior a 70, la asignatura no se aprueba
    # (es decir, nota <= 70 significa que debe repetirse)
    if nota <= 70:
        para_repetir.append(asignatura)

# 4. Mostramos el resultado final
print("\n--- RESULTADO DE EVALUACIÓN ---")
if len(para_repetir) > 0:
    print("Tienes que repetir las siguientes asignaturas:")
    for asignatura in para_repetir:
        print(f"- {asignatura}")
else:
    print("¡Felicidades! Aprobaste todas las asignaturas.")