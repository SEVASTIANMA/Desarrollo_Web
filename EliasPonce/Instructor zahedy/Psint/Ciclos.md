Algoritmo Contador_Ascendente
	// PARTE 1: Declaración e inicio del ciclo.
	// Se crea la variable 'i' como contador. El ciclo 'Para' inicializa 'i' en 1
	// y se ejecutará sucesivamente hasta que llegue a 10, aumentando de 1 en 1.
	Definir i Como Entero
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		
		// PARTE 2: Cuerpo del ciclo y fin.
		// En cada vuelta del bucle se imprime el valor actual de 'i'.
		// Al llegar a 10, el ciclo 'FinPara' se detiene y el programa termina.
		Escribir "Número: ", i
	FinPara
FinAlgoritmo
Algoritmo Validar_Contrasena
	// PARTE 1: Inicialización y condición de entrada.
	// Se define la variable 'clave' como texto y se inicializa vacía. El ciclo
	// 'Mientras' verifica si es diferente a '1234' para decidir si entra al bucle.
	Definir clave Como Texto
	clave <- ""
	Mientras clave != "1234" Hacer
		
		// PARTE 2: Petición de datos y validación.
		// Solicita la clave al usuario. Si el usuario se equivoca, el bucle se repite.
		// Si escribe '1234', la condición se rompe, sale del ciclo y da el acceso.
		Escribir "Introduce la contraseña correcta:"
		Leer clave
	FinMientras
	Escribir "¡Acceso concedido!"
FinAlgoritmo
Algoritmo Suma_Numeros_Positivos
	// PARTE 1: Inicialización de variables.
	// Creamos 'num' para leer los datos y 'acumulador' para guardar la suma.
	// El acumulador debe iniciar en 0 para no alterar la operación matemática.
	Definir num, acumulador Como Entero
	acumulador <- 0
	Repetir
		
		// PARTE 2: Entrada de datos, acumulación y condición de salida.
		// El programa pide un número. Si es positivo (mayor a 0), lo suma al total.
		// El ciclo se repite "Hasta Que" el usuario introduzca un número negativo (menor que 0).
		Escribir "Introduce un número a sumar (o uno negativo para salir):"
		Leer num
		Si num > 0 Entonces
			acumulador <- acumulador + num
		FinSi
	Hasta Que num < 0
	Escribir "La suma total de los números positivos es: ", acumulador
FinAlgoritmo
