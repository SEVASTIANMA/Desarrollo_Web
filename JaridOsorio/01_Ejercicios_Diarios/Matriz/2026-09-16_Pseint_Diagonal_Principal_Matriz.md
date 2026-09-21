Proceso DiagonalPrincipalMatriz
	Definir i, j, n, sumaDiagonal Como Entero
	n <- 3
	Dimension mat[n, n]
	
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Escribir "Ingrese valor [", i, ",", j, "]:"
			Leer mat[i, j]
		FinPara
	FinPara
	
	sumaDiagonal <- 0
	Escribir "--- ELEMENTOS DE LA DIAGONAL PRINCIPAL ---"
	Para i <- 1 Hasta n Hacer
		Escribir "Posicion [", i, ",", i, "]: ", mat[i, i]
		sumaDiagonal <- sumaDiagonal + mat[i, i]
	FinPara
	
	Escribir "Suma total de la diagonal principal: ", sumaDiagonal
FinProceso
