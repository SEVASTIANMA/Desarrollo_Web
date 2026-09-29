notas = [float(input(f"Ingresa la nota {i+1}: ")) for i in range(5)]
suma = sum(notas)
promedio = suma / len(notas)

print("--- CALCULADORA DE PROMEDIO ---")
print(f"Notas ingresadas: {notas}")
print(f"Suma total: {suma:.2f}")
print(f"El promedio final es: {promedio:.2f}")