Proceso MatrizTranspuesta
	Definir f, c, filas, columnas Como Entero
	filas <- 2; columnas <- 3
	Dimension orig[filas, columnas], trans[columnas, filas]
	
	// Llenado de matriz original
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir "Ingrese valor [", f, ",", c, "]:"
			Leer orig[f, c]
		FinPara
	FinPara
	
	// Transposición (Filas pasan a ser Columnas)
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			trans[c, f] <- orig[f, c]
		FinPara
	FinPara
	
	Escribir "--- MATRIZ TRANSPUESTA (3x2) ---"
	Para f <- 1 Hasta columnas Hacer
		Para c <- 1 Hasta filas Hacer
			Escribir Sin Saltar trans[f, c], " "
		FinPara
		Escribir ""
	FinPara
FinProceso