
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
repetir = []

for asignatura in asignaturas:
    nota = float(input("¿Qué nota sacaste en " + asignatura + "? "))

    if nota < 3.0:
        repetir.append(asignatura)

print("\nAsignaturas que tienes que repetir:")

if len(repetir) > 0:
    for asignatura in repetir:
        print(asignatura)
else:
    print("¡Has aprobado todas las asignaturas! :D")
