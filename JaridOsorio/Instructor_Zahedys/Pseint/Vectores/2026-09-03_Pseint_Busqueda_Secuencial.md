Proceso BusquedaSecuencial
	Definir n, i, buscar, contador Como Entero
	Escribir "Ingrese la cantidad de elementos en el vector:"
	Leer n
	Dimension datos[n]
	
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese dato para la posicion ", i, ":"
		Leer datos[i]
	FinPara
	
	Escribir "Ingrese el numero que desea buscar:"
	Leer buscar
	
	contador <- 0
	Para i <- 1 Hasta n Hacer
		Si datos[i] = buscar Entonces
			contador <- contador + 1
			Escribir "-> Encontrado en la posicion ", i
		FinSi
	FinPara
	
	Escribir "--------------------------------"
	Escribir "El numero ", buscar, " aparece ", contador, " vez/veces en el vector."
FinProceso