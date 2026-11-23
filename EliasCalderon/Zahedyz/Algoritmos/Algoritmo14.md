# Explicación del Algoritmo "Contador"

Este algoritmo tiene como objetivo **contar cuántos números positivos** introduce un usuario consecutivamente por teclado. El programa se detiene inmediatamente cuando se ingresa un número menor o igual a cero (0 o negativos).

---

## Estructura y Funcionamiento Paso a Paso

### 1. Entrada Inicial de Datos
El algoritmo comienza mostrando un encabezado decorativo en la pantalla y solicita al usuario que ingrese el primer número.
* **`Leer num`**: Captura el primer valor introducido por el usuario y lo almacena en la variable `num`.
* **`cont <- 0`**: Inicializa la variable `cont` (el contador) en cero.

### 2. El Ciclo de Control (`Mientras`)
El flujo principal del programa está gobernado por un bucle condicional:
```pseint
Mientras num > 0 Hacer
```
* **Condición de permanencia:** El ciclo se ejecutará de forma repetitiva **únicamente si** el número almacenado en `num` es estrictamente mayor que cero (un número positivo).
* Si el primer número ingresado por el usuario es `0` o un negativo, el ciclo nunca se ejecuta y el programa salta directamente al final.

### 3. Acciones dentro del Ciclo
Cada vez que el usuario introduce un número positivo, se ejecutan las siguientes instrucciones en orden:

* **Incremento del contador (`cont = cont + 1`):** Se le suma 1 al total de números positivos registrados.
* **Solicitud del siguiente número (`Leer num`):** El programa vuelve a pedir otro número para actualizar la variable `num`.
* **Evaluación de número negativo (`Si num < 0 Entonces`):** Revisa de inmediato si el nuevo número ingresado es negativo. Si se cumple, muestra en pantalla el mensaje informativo `"Numero negativo"`.

### 4. Condición de Salida y Resultado Final
* Cuando el usuario digita un número que **no es positivo** (por ejemplo, `0` o `-5`), el bloque del `Mientras` llega a su fin. En la siguiente comprobación, la condición `num > 0` se vuelve falsa y el bucle se rompe.
* Finalmente, el programa ejecuta la última línea:
  ```pseint
  Escribir 'valores positivos totales digitados: ' cont
  ```
  Mostrando en la pantalla la cantidad exacta de números positivos que se lograron contabilizar antes de salir.


Algoritmo Contador
	Escribir '==========================='
	Escribir '     Digite un numero'
	Escribir '==========================='
	Leer num
	cont <- 0
	
	Mientras num > 0 Hacer
		cont = cont + 1
		
		Escribir 'Digite un numero'
		Leer num
		
		si num < 0 Entonces
			
			Escribir 'Numero negativo'
		FinSi
		
		
	FinMientras
	Escribir 'valores positivos totales digitados: ' cont
	
FinAlgoritmo