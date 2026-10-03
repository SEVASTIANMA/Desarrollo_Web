Proceso SumaFilasColumnasMatriz
	Definir f, c, filas, columnas, sumaF, sumaC Como Entero
	filas <- 3; columnas <- 3
	Dimension mat[filas, columnas]
	
	// Lectura de datos
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir "Valor [", f, ",", c, "]:"
			Leer mat[f, c]
		FinPara
	FinPara
	
	// Suma por Filas
	Escribir "--- SUMA DE FILAS ---"
	Para f <- 1 Hasta filas Hacer
		sumaF <- 0
		Para c <- 1 Hasta columnas Hacer
			sumaF <- sumaF + mat[f, c]
		FinPara
		Escribir "Suma Fila ", f, ": ", sumaF
	FinPara
	
	// Suma por Columnas
	Escribir "--- SUMA DE COLUMNAS ---"
	Para c <- 1 Hasta columnas Hacer
		sumaC <- 0
		Para f <- 1 Hasta filas Hacer
			sumaC <- sumaC + mat[f, c]
		FinPara
		Escribir "Suma Columna ", c, ": ", sumaC
	FinPara
FinProceso