Proceso PromedioEstudiantesMatriz
	Definir est, notas, i, j Como Entero
	Definir suma, prom Como Real
	est <- 3; notas <- 3
	Dimension boletin[est, notas]
	
	Para i <- 1 Hasta est Hacer
		Escribir "--- Estudiante ", i, " ---"
		Para j <- 1 Hasta notas Hacer
			Escribir "Ingrese nota ", j, ":"
			Leer boletin[i, j]
		FinPara
	FinPara
	
	Escribir "---------------------------------------------"
	Escribir "--- PROMEDIOS FINALES ---"
	Para i <- 1 Hasta est Hacer
		suma <- 0
		Para j <- 1 Hasta notas Hacer
			suma <- suma + boletin[i, j]
		FinPara
		prom <- suma / notas
		Escribir "Estudiante ", i, " - Promedio: ", prom
	FinPara
FinProceso