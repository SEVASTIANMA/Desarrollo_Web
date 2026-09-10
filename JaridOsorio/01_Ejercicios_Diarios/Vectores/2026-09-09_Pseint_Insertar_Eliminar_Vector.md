Proceso InsertarYEliminarEnVector
	Definir tam, maxTam, i, posInsertar, valInsertar, posEliminar, opcion Como Entero
	maxTam <- 10
	Dimension vec[maxTam]
	
	// Vector inicial con 5 elementos de prueba
	tam <- 5
	vec[1]<-10; vec[2]<-20; vec[3]<-30; vec[4]<-40; vec[5]<-50
	
	Escribir "--- VECTOR INICIAL ---"
	Para i <- 1 Hasta tam Hacer
		Escribir "Posicion ", i, ": ", vec[i]
	FinPara
	
	Escribir "---------------------------------------------"
	Escribir "Elija una operacion: 1. Insertar | 2. Eliminar"
	Leer opcion
	
	Si opcion = 1 Entonces
		Si tam < maxTam Entonces
			Escribir "Ingrese la posicion a insertar (1 a ", tam + 1, "):"
			Leer posInsertar
			Escribir "Ingrese el valor:"
			Leer valInsertar
			
			// Desplazamiento hacia la derecha
			Para i <- tam Hasta posInsertar Con Paso -1 Hacer
				vec[i + 1] <- vec[i]
			FinPara
			
			vec[posInsertar] <- valInsertar
			tam <- tam + 1
			Escribir "¡Elemento insertado con exito!"
		Sino
			Escribir "El vector esta lleno, no se pueden insertar mas elementos."
		FinSi
		
	Sino Si opcion = 2 Entonces
		Escribir "Ingrese la posicion a eliminar (1 a ", tam, "):"
		Leer posEliminar
		
		// Desplazamiento hacia la izquierda
		Para i <- posEliminar Hasta tam - 1 Hacer
			vec[i] <- vec[i + 1]
		FinPara
		
		tam <- tam - 1
		Escribir "¡Elemento eliminado con exito!"
	FinSi
	
	// Mostrar vector resultante
	Escribir "---------------------------------------------"
	Escribir "--- VECTOR RESULTANTE ---"
	Para i <- 1 Hasta tam Hacer
		Escribir "Posicion ", i, ": ", vec[i]
	FinPara
FinProceso