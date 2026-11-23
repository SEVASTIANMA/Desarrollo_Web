Proceso PromedioParesImpares
	Definir n, i, sumaPares, cantPares, sumaImpares, cantImpares Como Entero
	Escribir "Ingrese la cantidad de elementos:"
	Leer n
	Dimension numeros[n]
	
	sumaPares <- 0; cantPares <- 0
	sumaImpares <- 0; cantImpares <- 0
	
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese el valor ", i, ":"
		Leer numeros[i]
		
		Si numeros[i] % 2 = 0 Entonces
			sumaPares <- sumaPares + numeros[i]
			cantPares <- cantPares + 1
		Sino
			sumaImpares <- sumaImpares + numeros[i]
			cantImpares <- cantImpares + 1
		FinSi
	FinPara
	
	Escribir "--- RESULTADOS ---"
	Si cantPares > 0 Entonces
		Escribir "Promedio de numeros pares: ", (sumaPares / cantPares)
	Sino
		Escribir "No se ingresaron numeros pares."
	FinSi
	
	Si cantImpares > 0 Entonces
		Escribir "Promedio de numeros impares: ", (sumaImpares / cantImpares)
	Sino
		Escribir "No se ingresaron numeros impares."
	FinSi
FinProceso