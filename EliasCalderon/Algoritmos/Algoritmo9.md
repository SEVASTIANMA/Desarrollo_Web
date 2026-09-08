# Explicación del Algoritmo "SuCuadrado"

Este algoritmo procesa números ingresados por el usuario para calcular su cuadrado de forma cíclica, finalizando su ejecución cuando se introduce un valor menor o igual a cero.

## Estructura y Componentes

### 1. Inicialización y Entrada Inicial
* **`Escribir 'Digite un numero'`**: Muestra un mensaje en pantalla solicitando un dato al usuario.
* **`Leer num`**: Captura el valor introducido por teclado y lo almacena en la variable `num`.

### 2. Ciclo Principal (`Mientras num > 0 Hacer`)
El bucle evalúa el valor de `num` antes de ejecutar el código en su interior. Si el número es mayor que cero, realiza las siguientes acciones secuenciales:

* **Cálculo del Cuadrado:** La instrucción `Escribir num * num` calcula y muestra directamente el resultado de multiplicar el número por sí mismo.
* **Actualización de la Variable:** Solicita un nuevo número al usuario (`Escribir` y `Leer num`) para actualizar el estado del ciclo.
* **Condicional Interno (`si num < 0 Entonces`):** Evalúa si el nuevo número ingresado es negativo. Si se cumple, muestra el mensaje `"Su numero es negativo"`.

### 3. Finalización del Algoritmo
El algoritmo termina cuando la condición del ciclo `Mientras num > 0` deja de cumplirse. Esto ocurre en dos escenarios:
1. Si el usuario digita un número **negativo** (el condicional interno avisa que es negativo y luego el ciclo se rompe al comprobar que no es mayor a cero).
2. Si el usuario digita el número **cero** (el ciclo se rompe directamente sin activar el condicional interno).



Algoritmo SuCuadrado
	Escribir 'Digite un numero'
	Leer num
	Mientras num > 0 Hacer
		Escribir num * num
		Escribir 'Digite un numero'
		Leer num
		si num < 0 Entonces
			
		Escribir 'Su numero es negativo'
		FinSi
		
	FinMientras
	
	
FinAlgoritmo