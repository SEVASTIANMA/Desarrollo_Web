Algoritmo TiendaVir

// Este algoritmo permite ingresar un menu virtual el cual al ingresar el digito 4 este salga del menu para dar el resultado total de cuanto debe pagar y la cantidad de elementos que se llevo

	n = 0
	m = 0
	TotalM = 0
	l = 0
	
	Repetir
		escribir'-----TIENDA VIRTUAL-----'
		escribir'Ingrese el elemento que se quiera llevar (O ingrese 4 para salir del menu)'
		escribir'1. Salchipapa - 8000'
		escribir'2. Perro Caliente - 7000'
		escribir'3. Hamburguesa - 12000'
		leer n
		
		si n <> 4 entonces
		escribir'Ingrese el precio'
		leer m
		l = l + 1
		finsi
		
		si n < 1 o n > 4 Entonces
			escribir 'ERROR. Numero no identificado por favor intentelo de nuevo.'
			leer n
		FinSi
		
		TotalM = TotalM + m
		
		
	Hasta Que n = 4
	
	escribir 'Has seleccionado ' l ' articulos.'
	escribir'Total a pagar: ' TotalM '.'
FinAlgoritmo
