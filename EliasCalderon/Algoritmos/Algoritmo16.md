Algoritmo contarNum
	Definir numero0 como entero
	Escribir 'Digite su numero del 0 al 9.999: '
	Leer numero0
	si numero0 < 0 o numero0 > 9999 Entonces
		Escribir 'Numero fuera de rango'
	sino
		Si numero0 < 10 Entonces
			Escribir 'Tiene 1 cifra'
		Sino
			Si numero0 < 100 Entonces
				Escribir 'Tiene 2 cifras'
			Sino
				Si numero0 < 1000 Entonces
					Escribir 'Tiene 3 cifras'
				Sino
					Escribir 'Tiene 4 cifras'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo


# Explicación del Algoritmo: contarNum

Este algoritmo tiene como objetivo determinar la cantidad de dígitos (cifras) que tiene un número entero ingresado por el usuario, siempre y cuando este número se encuentre en un rango específico de 0 a 9,999.

## Estructura y Funcionamiento Paso a Paso

1. **Definición de Variables:**
   * Se crea una variable llamada `numero0` de tipo entero para almacenar el valor que introduzca el usuario.

2. **Entrada de Datos:**
   * El programa muestra el mensaje "Digite su numero del 0 al 9.999: " y espera a que el usuario escriba un valor.

3. **Validación de Rango:**
   * La primera condición evalúa si el número es menor que 0 o mayor que 9,999 (`numero0 < 0 o numero0 > 9999`).
   * Si se cumple esta condición, el programa muestra el mensaje "Numero fuera de rango" y finaliza.

4. **Conteo de Cifras (Condicionales Anidados):**
   Si el número es válido, pasa por una serie de descartes lógicos de menor a mayor:
   * **1 cifra:** Si es menor a 10 (números del 0 al 9).
   * **2 cifras:** Si no fue menor a 10, pero es menor a 100 (números del 10 al 99).
   * **3 cifras:** Si no fue menor a 100, pero es menor a 1,000 (números del 100 al 999).
   * **4 cifras:** Si no cumple ninguna de las anteriores (números del 1,000 al 9,999).

---

## Resumen de Salidas

| Rango del Número | Resultado en Pantalla |
| :--- | :--- |
| Menor que 0 o Mayor que 9999 | Numero fuera de rango |
| De 0 a 9 | Tiene 1 cifra |
| De 10 a 99 | Tiene 2 cifras |
| De 100 a 999 | Tiene 3 cifras |
| De 1000 a 9999 | Tiene 4 cifras |
