Algoritmo LlenarVector

// Este algoritmo permite guardar 5 números en un arreglo (vector) y luego los muestra en pantalla junto con su promedio.

	Definir numeros, i, suma Como Entero
	Definir promedio Como Real
	Dimension numeros[5]
	
	suma <- 0
	
	Para i <- 1 Hasta 4 Con Paso 1 Hacer
		Escribir "Ingrese el número para la posición ", i, ":"
		Leer numeros[i]
		suma <- suma + numeros[i]
	FinPara

    promedio <- suma / 5
	
	Escribir "--- Los números ingresados son: ---"
	Para i <- 1 Hasta 4 Con Paso 1 Hacer
		Escribir "Posición ", i, ": ", numeros[i]
	FinPara
	
	Escribir "El promedio total es: ", promedio
    
FinAlgoritmo

