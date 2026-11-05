# Explicación del Algoritmo "HastaNegativo"

Este algoritmo tiene como objetivo solicitar números al usuario de forma repetitiva y contar cuántas entradas se realizaron, deteniendo su ejecución en el momento en que se introduce un número negativo.

## Estructura y Funcionamiento

1. **Inicialización implícita**: El algoritmo utiliza una variable llamada `contador`. Aunque no se muestra explícitamente su inicialización en cero, se asume que empieza en 0 para llevar el registro de las iteraciones.
2. **Bucle Repetir-Hasta Que**: Es una estructura de control de ciclos que asegura que las instrucciones de su interior se ejecuten al menos una vez.
   * **Mostrar mensaje**: Se imprime en pantalla el texto 'digite numero' para dar una instrucción al usuario.
   * **Lectura de datos**: Se guarda el valor ingresado por el usuario en la variable `num`.
   * **Incremento del contador**: La instrucción `contador = contador + 1` suma una unidad al total de números registrados cada vez que se pasa por el ciclo.
   * **Condición de parada**: El bucle se evalúa al final de cada iteración con `Hasta Que num < 0`. Si el número ingresado es menor a cero (negativo), el bucle se rompe. Si es cero o positivo, el ciclo vuelve a empezar.
3. **Resultado final**: Fuera del bucle, la instrucción `Escribir 'Hay' contador 'numeros'` muestra en pantalla la cantidad total de números introducidos por el usuario durante la ejecución, incluyendo el número negativo que causó el cierre del programa.




Algoritmo HastaNegativo
	repetir
		escribir 'digite numero'
		Leer num
		contador = contador + 1
	Hasta Que num < 0
	Escribir 'Hay' contador 'numeros'
FinAlgoritmo