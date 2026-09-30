Proceso MatrizTriangularSuperior
	Definir n, i, j Como Entero
	Definir esTriangular Como Logico
	n <- 3
	Dimension mat[n, n]
	
	// Lectura de la matriz
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Escribir "Valor [", i, ",", j, "]:"
			Leer mat[i, j]
		FinPara
	FinPara
	
	// Verificacion: los elementos debajo de la diagonal (i > j) deben ser 0
	esTriangular <- Verdadero
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Si i > j Y mat[i, j] <> 0 Entonces
				esTriangular <- Falso
			FinSi
		FinPara
	FinPara
	
	Escribir "---------------------------------------------"
	Si esTriangular Entonces
		Escribir "La matriz ES triangular superior."
	Sino
		Escribir "La matriz NO es triangular superior."
	FinSi
FinProceso