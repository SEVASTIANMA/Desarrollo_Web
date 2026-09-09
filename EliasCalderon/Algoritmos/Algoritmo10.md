# Explicación del Algoritmo "PosONeng"

Este algoritmo evalúa si un número real es positivo o negativo mediante una estructura condicional.

## Flujo de ejecución paso a paso:

1. **Definición de variables (`Definir num1 Como Real`)**: 
   Se crea una variable llamada `num1` que puede almacenar números reales (incluyendo decimales).
2. **Entrada de datos (`Escribir` y `Leer`)**: 
   El programa muestra el mensaje `"Digite un numero"` en la pantalla y detiene la ejecución hasta que el usuario introduce un valor, el cual se guarda en `num1`.
3. **Estructura condicional (`Si... Entonces... SiNo`)**:
   * **Condición (`Si num1 >= 0`)**: Comprueba si el número ingresado es mayor o igual a cero.
   * **Bloque Verdadero**: Si la condición se cumple, se ejecuta la instrucción que muestra el mensaje `"Este numero es positivo"`.
   * **Bloque Falso (`SiNo`)**: Si el número es menor que cero, el flujo va por este camino y muestra el mensaje `"Este numero es negativo"`.
4. **Fin del programa (`FinAlgoritmo`)**: Termina la ejecución del código.


Algoritmo PosONeng
		Definir num1 Como Real
		Escribir 'Digite un numero'
		Leer num1
		Si num1 >= 0 Entonces
			Escribir 'Este numero es positivo'
		SiNo
			Escribir 'Este numero es negativo'
		FinSi
FinAlgoritmo