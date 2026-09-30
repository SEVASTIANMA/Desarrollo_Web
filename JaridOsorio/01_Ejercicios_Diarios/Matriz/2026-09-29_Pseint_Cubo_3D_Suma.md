Proceso SumaCubo3D
	Definir k, i, j, sumaTotal Como Entero
	Dimension cubo[2, 2, 2]
	
	cubo[1,1,1]<-5; cubo[1,1,2]<-3; cubo[1,2,1]<-2; cubo[1,2,2]<-4
	cubo[2,1,1]<-1; cubo[2,1,2]<-6; cubo[2,2,1]<-8; cubo[2,2,2]<-7
	
	sumaTotal <- 0
	Para k <- 1 Hasta 2 Hacer
		Para i <- 1 Hasta 2 Hacer
			Para j <- 1 Hasta 2 Hacer
				sumaTotal <- sumaTotal + cubo[k, i, j]
			FinPara
		FinPara
	FinPara
	
	Escribir "La suma total de todos los elementos del cubo 3D es: ", sumaTotal
FinProceso