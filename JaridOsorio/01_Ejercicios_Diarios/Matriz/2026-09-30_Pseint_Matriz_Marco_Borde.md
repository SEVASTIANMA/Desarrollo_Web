Proceso MatrizMarcoBorde
	Definir f, c, filas, columnas Como Entero
	filas <- 5; columnas <- 5
	Dimension mat[filas, columnas]
	
	// Generar matriz con bordes en 1 y centro en 0
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Si f = 1 O f = filas O c = 1 O c = columnas Entonces
				mat[f, c] <- 1
			Sino
				mat[f, c] <- 0
			FinSi
		FinPara
	FinPara
	
	Escribir "--- MATRIZ CON MARCO 5x5 ---"
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir Sin Saltar mat[f, c], " "
		FinPara
		Escribir ""
	FinPara
FinProceso