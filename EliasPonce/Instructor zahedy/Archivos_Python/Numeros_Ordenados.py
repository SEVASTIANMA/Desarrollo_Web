import random

# --- DIMENSIONAR Y DEFINIR VARIABLES ---
# En Python no es necesario declarar tipos de variables, se crean al usarse.
# Inicializamos el vector con ceros para reservar los 100 espacios.
vector = [0] * 100

# 1. Llenar el vector con números del 1 al 100
for i in range(100):
    vector[i] = i + 1

# 2. Desordenar el vector de manera aleatoria
for i in range(100):
    # random.randint(0, 99) genera un número entero aleatorio entre 0 y 99 inclusive
    posicion_aleatoria = random.randint(0, 99)
    
    # Intercambiar valores usando una variable auxiliar (idéntico a PSeInt)
    auxiliar = vector[i]
    vector[i] = vector[posicion_aleatoria]
    vector[posicion_aleatoria] = auxiliar

print("--- NÚMEROS DESORDENADOS ---")
for i in range(100):
    print(vector[i])

# 3. Ordenar de manera ASCENDENTE (Método Burbuja)
for i in range(99):
    for j in range(100 - i - 1):
        if vector[j] > vector[j + 1]:
            # Intercambio de posiciones
            auxiliar = vector[j]
            vector[j] = vector[j + 1]
            vector[j + 1] = auxiliar

print("--- NÚMEROS ORDENADOS ASCENDENTE ---")
for i in range(100):
    print(vector[i])
