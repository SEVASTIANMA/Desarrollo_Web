Proceso MayorMenorVector
	Definir n, i, mayor, posMayor, menor, posMenor Como Entero
	Escribir "Ingrese la cantidad de elementos del vector:"
	Leer n
	Dimension vec[n]
	
	// Lectura de datos
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese el valor para la posicion ", i, ":"
		Leer vec[i]
	FinPara
	
	// Inicialización con el primer elemento
	mayor <- vec[1]
	posMayor <- 1
	menor <- vec[1]
	posMenor <- 1
	
	// Recorrido para comparar
	Para i <- 2 Hasta n Hacer
		Si vec[i] > mayor Entonces
			mayor <- vec[i]
			posMayor <- i
		FinSi
		
		Si vec[i] < menor Entonces
			menor <- vec[i]
			posMenor <- i
		FinSi
	FinPara
	
	// Mostrar resultados
	Escribir "---------------------------------------------"
	Escribir "El numero MAYOR es: ", mayor, " en la posicion ", posMayor
	Escribir "El numero MENOR es: ", menor, " en la posicion ", posMenor
FinProceso