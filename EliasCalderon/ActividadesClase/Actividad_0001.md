## PYTHON

notas = []

for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Introduce la nota {i}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

promedio = sum(notas) / len(notas)
print(f"\nEl promedio de las 5 notas es: {round(promedio, 2)}")

## DART


