Proceso RotacionVector
	Definir n, i, k, des, aux, opcion Como Entero
	Escribir "Ingrese la cantidad de elementos en el vector:"
	Leer n
	Dimension vec[n]
	
	// Carga de datos
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese el elemento ", i, ":"
		Leer vec[i]
	FinPara
	
	Escribir "---------------------------------------------"
	Escribir "Seleccione la direccion de rotacion:"
	Escribir "1. Derecha"
	Escribir "2. Izquierda"
	Leer opcion
	
	Escribir "Ingrese el numero de posiciones a desplazar:"
	Leer des
	
	// Aplicar modulo para evitar desplazamientos redundantes
	des <- des % n
	
	Para k <- 1 Hasta des Hacer
		Si opcion = 1 Entonces
			// Rotacion a la Derecha
			aux <- vec[n]
			Para i <- n Hasta 2 Con Paso -1 Hacer
				vec[i] <- vec[i - 1]
			FinPara
			vec[1] <- aux
		Sino Si opcion = 2 Entonces
			// Rotacion a la Izquierda
			aux <- vec[1]
			Para i <- 1 Hasta n - 1 Hacer
				vec[i] <- vec[i + 1]
			FinPara
			vec[n] <- aux
		FinSi
	FinPara
	
	// Resultado
	Escribir "--- VECTOR ROTADO ---"
	Para i <- 1 Hasta n Hacer
		Escribir "Posicion ", i, ": ", vec[i]
	FinPara
FinProceso