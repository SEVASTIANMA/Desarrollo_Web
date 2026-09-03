# Explicación del Algoritmo "NumPrimo"

Este algoritmo evalúa si un número entero positivo es primo. Un número es primo si solo tiene dos divisores positivos: el **1** y **él mismo**.

## Componentes del Código

### 1. Entrada de Datos
```pseudocode
Escribir 'Digite un numero'
Leer num
```
* Solicita al usuario que ingrese un número y lo almacena en la variable `num`.

### 2. Inicialización de Variables
```pseudocode
i = 1
```
* Crea un contador `i` que inicia en 1. Este contador se usará para probar todos los números desde 1 hasta el número ingresado.
* *Nota:* La variable `divisor` no se inicializa explícitamente en 0 en el código, pero el algoritmo asume que arranca vacía para contar los divisores encontrados.

### 3. Bucle de Simulación (Mientras)
```pseudocode
mientras i <= num
    si (num mod i = 0)
        divisor = divisor + 1
    FinSi
    i = i + 1
FinMientras
```
* **Condición:** El ciclo se repite mientras `i` sea menor o igual a `num`.
* **Operación Mod (Residuo):** `num mod i = 0` verifica si la división es exacta (residuo cero). Si es exacta, significa que `i` es un divisor de `num`.
* **Contador de Divisores:** Cada vez que encuentra una división exacta, aumenta la variable `divisor` en 1.
* **Incremento:** Se suma 1 a `i` para evaluar el siguiente número en la próxima vuelta.

### 4. Evaluación y Resultado
```pseudocode
si divisor <= 2 Entonces
    Escribir 'El numero es primo'
SiNo
    escribir 'El numero no es primo'
FinSi
```
* Al terminar el bucle, se revisa cuántos divisores se encontraron.
* Si el número de divisores es **menor o igual a 2** (específicamente 2 para números mayores que 1), el algoritmo concluye que el número es **primo**.
* Si tiene más de 2 divisores, concluye que **no es primo**.



Algoritmo NumPrimo
	Escribir 'Digite un numero'
	Leer num
	i = 1
	mientras i <= num
		si (num mod i = 0)
			divisor = divisor + 1
		FinSi
		i = i + 1
	FinMientras
	si divisor <= 2 Entonces
		Escribir 'El numero es primo'
	SiNo
		escribir 'El numero no es primo'
	FinSi
FinAlgoritmo