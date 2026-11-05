Algoritmo Promedio
	Definir notas, i, j, suma Como Real
	Dimension notas[3,3]

	Para i <- 1 Hasta 3 Hacer
		suma <- 0
		Para j <- 1 Hasta 3 Hacer
			Leer notas[i,j]
			suma <- suma + notas[i,j]
		FinPara
		Escribir "Promedio: ", suma/3
	FinPara
FinAlgoritmo