# Explicación del Algoritmo: Múltiplos en PSeInt

Este algoritmo tiene como objetivo determinar si dos números ingresados por el usuario son múltiplos entre sí. Utiliza la operación matemática del residuo para verificar si una división es exacta.

---

## Funcionamiento Paso a Paso

1. Definiendo Variables: Se reservan los espacios en memoria para almacenar los dos números (num1 y num2) como números reales (con decimales).
2. Interfaz de Usuario: El programa muestra un menú visual con líneas (====) solicitando al usuario que introduzca los valores.
3. Lectura de Datos: El programa se detiene y espera a que el usuario digite el primer número y luego el segundo, guardándolos en sus respectivas variables.
4. Evaluación de la Condición (MOD): 
   * Utiliza el operador mod (módulo), el cual calcula el residuo de una división entera.
   * Si num1 mod num2 = 0, significa que num1 se puede dividir exactamente entre num2.
   * Si num2 mod num1 = 0, significa que num2 se puede dividir exactamente entre num1.
   * Al usar el conector lógico "o", basta con que una de las dos condiciones sea verdadera para que los números se consideren múltiplos.
5. Resultado: Si la división es exacta, el programa muestra en pantalla que sí son múltiplos; de lo contrario, indica que no lo son.

---

## Notas y Correcciones del Código Original

El código original presentaba dos detalles técnicos importantes que se deben corregir para que funcione correctamente en PSeInt:

* Falta definir num2: En la línea Definir num1 Como Real, faltaba agregar la variable num2.
* Mensaje de salida: El mensaje final dice siempre 'Es multiplo de: ' num2. Esto puede ser confuso si, por ejemplo, ingresas 2 y 10, ya que 2 no es múltiplo de 10, sino al revés. Una redacción más clara sería simplemente decir "Los números son múltiplos entre sí".


Algoritmo multiplodelNUM
	Definir num1 Como Real
	Escribir '================================'
	Escribir '     Digite sus numeros'
	Escribir '================================'
	Leer num1
	Leer num2
	si num1 mod num2 = 0 o num2 mod num1 = 0 Entonces
		
		Escribir 'Es multiplo de: ' num2
	SiNo
		Escribir 'No es multiplo de: ' num2
	FinSi
FinAlgoritmo