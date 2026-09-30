Proceso MultiplicacionMatrizEscalar
	Definir f, c, filas, columnas, escalar Como Entero
	filas <- 3; columnas <- 3
	Dimension mat[filas, columnas], resultado[filas, columnas]
	
	// Carga de datos
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir "Ingrese valor [", f, ",", c, "]:"
			Leer mat[f, c]
		FinPara
	FinPara
	
	Escribir "Ingrese el escalar (numero por el cual multiplicar la matriz):"
	Leer escalar
	
	// Multiplicación por escalar
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			resultado[f, c] <- mat[f, c] * escalar
		FinPara
	FinPara
	
	Escribir "--- MATRIZ RESULTANTE ---"
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir Sin Saltar resultado[f, c], " "
		FinPara
		Escribir ""
	FinPara
FinProceso