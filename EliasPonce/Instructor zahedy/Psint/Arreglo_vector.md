Algoritmo sin_titulo
	Definir vector Como Entero
    Definir i, suma Como Entero
    Definir promedio Como Real
    
    Dimension vector[10]
    
    suma <- 0
    
    // Ingresar los 10 números
	Para i <- 1 Hasta 10 Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer vector[i]
        suma <- suma + vector[i]
    FinPara
    
    // Mostrar el vector original
    Escribir ""
    Escribir "Vector original:"
    
    Para i <- 1 Hasta 10 Hacer
        Escribir Sin Saltar vector[i], " "
    FinPara
    
    // Calcular el promedio
    promedio <- suma / 10
    
    Escribir ""
    Escribir ""
    Escribir "La suma de los elementos es: ", suma
    Escribir "El promedio es: ", promedio

FinAlgoritmo
