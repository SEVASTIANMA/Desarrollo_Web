Algoritmo contarNum
	Definir numero0 como entero
	Escribir 'Digite su numero del 0 al 9.999: '
	Leer numero0
	si numero0 < 0 o numero0 > 9999 Entonces
		Escribir 'Numero fuera de rango'
	sino
		Si numero0 < 10 Entonces
			Escribir 'Tiene 1 cifra'
		Sino
			Si numero0 < 100 Entonces
				Escribir 'Tiene 2 cifras'
			Sino
				Si numero0 < 1000 Entonces
					Escribir 'Tiene 3 cifras'
				Sino
					Escribir 'Tiene 4 cifras'
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo