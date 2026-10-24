pila = []
print("--- Registro de Alumnos en Pila (Límite: suma edades < 100) ---")
edades = 0
while edades < 100:
    edad = int(input(f"\nEdad del alumno {len(pila) + 1}: "))
    estatura = float(input(f"Estatura del alumno {len(pila) + 1} (en m): "))
    pila.append((edad, estatura))
    edades += edad
alumnos = len(pila)
estaturas = mayores = altos = 0
while len(pila) > 0:
    alumno = pila.pop()
    estaturas += alumno[1]
    if alumno[0] > 18: 
        mayores += 1
    if alumno[1] > 1.75: 
        altos += 1
if alumnos > 0:
    print(f"Edad media: {(edades / alumnos):.2f} años")
    print(f"Estatura media: {(estaturas / alumnos):.2f} m")
    print(f"Alumnos mayores de 18: {mayores}")
    print(f"Alumnos de más de 1.75m: {altos}")