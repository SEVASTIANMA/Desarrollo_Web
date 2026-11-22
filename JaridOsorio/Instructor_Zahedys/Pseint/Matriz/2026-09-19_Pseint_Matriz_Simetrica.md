Proceso MatrizSimetrica
	Definir n, i, j Como Entero
	Definir esSimetrica Como Logico
	n <- 3
	Dimension mat[n, n]
	
	// Lectura de datos
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Escribir "Ingrese elemento [", i, ",", j, "]:"
			Leer mat[i, j]
		FinPara
	FinPara
	
	// Verificacion de simetria (mat[i,j] debe ser igual a mat[j,i])
	esSimetrica <- Verdadero
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Si mat[i, j] <> mat[j, i] Entonces
				esSimetrica <- Falso
			FinSi
		FinPara
	FinPara
	
	Escribir "---------------------------------------------"
	Si esSimetrica Entonces
		Escribir "La matriz ES simetrica."
	Sino
		Escribir "La matriz NO es simetrica."
	FinSi
FinProceso