Algoritmo sin_titulo
	escribir " longitud lad1 "
	leer a
	escribir " digite lad2 "
	leer b
	Escribir " digite lad4  "
	leer c
	triangulo = falso 
	si ( a >=  b) y ( a >= c ) Entonces
		si ( a <  b + c ) Entonces
			triangulo = verdadero 
		FinSi
	FinSi
	si ( b >=  a) y ( b >= c ) Entonces
		si ( b <  a + c ) Entonces
			triangulo = verdadero 
		FinSi
	FinSi
	si ( c >=  a) y ( c >= b ) Entonces
		si ( c <  a + b ) Entonces
			triangulo = verdadero 
		FinSi
	FinSi
	si triangulo = verdadero Entonces
		si ( a = b ) y ( b = c ) Entonces
			Escribir " triangulo equilatero "
		SiNo
			si ( a = b ) o ( b = c ) o ( a = c) Entonces
				Escribir " triangulo Isoceles "
			SiNo
				escribir " triangulo escaleno "
				
			FinSi
		FinSi
	sino 
		escribir " no es un triangulo "
	FinSi
	
	
FinAlgoritmo
