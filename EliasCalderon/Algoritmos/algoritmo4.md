## Cómo Funciona

El código utiliza una estructura de control repetitiva llamada Bucle Para (Para...Hasta...Con Paso). 

* **Secuencial:** Ejecuta 10 bloques independientes de código, uno tras otro.
* **Variable Controladora:** Utiliza la variable A en cada bloque como el multiplicador que va del 1 al 10.
* **Incremento:** El comando Con Paso 1 indica que la variable A aumenta de uno en uno en cada repetición.
* **Salida de Datos:** El comando Escribir muestra el texto formateado (ej. 5 * 3 = 15) calculando el resultado matemático al instante.

---

## Oportunidad de Optimización (Bucles Aninados)

El algoritmo actual funciona correctamente pero es redundante (repite el mismo bloque de código 10 veces). En programación, esto se puede optimizar drásticamente utilizando un bucle anidado (un bucle dentro de otro).



Algoritmo TablasdeMultiplicarx10
	para A = 1 hasta 10 con paso 1 
		Escribir ' 1 * ' A ' = ' 1 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 2 * ' A ' = ' 2 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 3 * ' A ' = ' 3 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 4 * ' A ' = ' 4 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 5 * ' A ' = ' 5 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 6 * ' A ' = ' 6 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 7 * ' A ' = ' 7 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 8 * ' A ' = ' 8 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 9 * ' A ' = ' 9 * A
	FinPara
	para A = 1 hasta 10 con paso 1 
		Escribir ' 10 * ' A ' = ' 10 * A
	FinPara
FinAlgoritmo