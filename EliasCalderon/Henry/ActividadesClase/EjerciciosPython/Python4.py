'''
# Explicación del Algoritmo en Python

Este algoritmo **solicita un número entero al usuario y genera un diccionario que contiene los cuadrados de todos los números desde el 1 hasta el número ingresado**.

A pesar de que la variable se llama `lista`, el código utiliza llaves `{}` y la estructura `llave: valor`, lo que en Python genera un **diccionario** mediante una técnica llamada *comprensión de diccionarios*.

---

## Desglose del Código línea por línea

### 1. Entrada de datos
```python
num = int(input('Digite su numero... '))
```
* `input(...)`: Muestra un mensaje en la consola y espera a que el usuario escriba algo.
* `int(...)`: Convierte el texto introducido por el usuario en un número entero para poder realizar operaciones matemáticas.

### 2. Generación del diccionario
```python
lista = {i: i**2 for i in range(1, num + 1)}
```
* `range(1, num + 1)`: Crea un rango numérico que inicia en `1` y termina exactamente en el número ingresado (`num`).
* `for i in...`: Un ciclo que recorre el rango número por número, asignando el valor actual a la variable temporal `i`.
* `i: i**2`: Define la estructura del diccionario. La llave es el número actual (`i`) y el valor es ese mismo número elevado al cuadrado (`i**2`).

### 3. Salida de datos
```python
print(lista)
```
* Imprime el diccionario resultante en la pantalla.

---

## Ejemplo Práctico de Ejecución

Si ejecutas el programa e ingresas el número **`4`**, el flujo interno será el siguiente:

* `i = 1` -> 1² = 1
* `i = 2` -> 2² = 4
* `i = 3` -> 3² = 9
* `i = 4` -> 4² = 16

**Resultado en consola:**
```python
{1: 1, 2: 4, 3: 9, 4: 16}

'''

num = int(input('Digite su numero... '))
lista = {i: i**2 for i in range (1, num + 1)}
print(lista)     
