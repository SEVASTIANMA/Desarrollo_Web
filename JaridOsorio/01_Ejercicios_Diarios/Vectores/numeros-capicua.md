Proceso VerificarNumeroCapicua
	Definir n, i Como Entero
	Definir esCapicua Como Logico
	
	Escribir "Ingrese la cantidad de digitos del numero:"
	Leer n
	
	Dimension digitos[n]
	
	// Llenado del vector con los dígitos del número
	Para i <- 1 Hasta n Hacer
		Escribir "Ingrese el digito en la posicion ", i, ":"
		Leer digitos[i]
	FinPara
	
	// Verificación de cápicua comparando extremos hacia el centro
	esCapicua <- Verdadero
	Para i <- 1 Hasta trunc(n / 2) Hacer
		Si digitos[i] <> digitos[n - i + 1] Entonces
			esCapicua <- Falso
		FinSi
	FinPara
	
	// Resultado
	Escribir "-----------------------------------"
	Si esCapicua Entonces
		Escribir "El numero ingresado ES capicua (se lee igual al derecho y al reves)."
	Sino
		Escribir "El numero ingresado NO es capicua."
	FinSi
FinProceso