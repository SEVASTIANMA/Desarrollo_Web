Algoritmo SumaNumeros
	
// Este algoritmo suma los primeros **N** números enteros positivos ingresados por el usuario utilizando un bucle Mientras.

		Definir n, contador, suma Como Entero
		
		Escribir "Ingrese un número entero positivo:"
		Leer n
		
		suma <- 0
		contador <- 1
		
		Mientras contador <= n Hacer
			suma <- suma + contador
			contador <- contador + 1
		FinMientras
		
		Escribir "La suma de los primeros ", n, " números es: ", suma

FinAlgoritmo
