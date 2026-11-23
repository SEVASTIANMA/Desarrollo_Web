Proceso MatrizIdentidad
	Definir n, i, j Como Entero
	n <- 4
	Dimension mat[n, n]
	
	// Generar Matriz Identidad (1s en diagonal principal, 0s en el resto)
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Si i = j Entonces
				mat[i, j] <- 1
			Sino
				mat[i, j] <- 0
			FinSi
		FinPara
	FinPara
	
	Escribir "--- MATRIZ IDENTIDAD 4x4 ---"
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Escribir Sin Saltar mat[i, j], " "
		FinPara
		Escribir ""
	FinPara
FinProceso