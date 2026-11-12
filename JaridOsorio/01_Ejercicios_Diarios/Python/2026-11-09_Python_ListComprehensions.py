# ==========================================
# Compresión de Listas en Python
# ==========================================

# Lista numérica original
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener únicamente los números pares usando List Comprehension
pares = [n for n in numeros if n % 2 == 0]

# Elevar al cuadrado los números impares
impares_cuadrado = [n ** 2 for n in numeros if n % 2 != 0]

print("--- RESULTADOS DE COMPRENSIÓN DE LISTAS ---")
print(f"Números originales: {numeros}")
print(f"Números pares filtrados: {pares}")
print(f"Impares al cuadrado: {impares_cuadrado}")