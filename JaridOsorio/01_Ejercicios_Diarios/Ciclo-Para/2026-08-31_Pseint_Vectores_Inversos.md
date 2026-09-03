Proceso InvertirVector
    Definir n, i Como Entero
    
    Escribir "Ingrese la cantidad de elementos del vector:"
    Leer n
    
    Dimension vec[n]
    
    Para i <- 1 Hasta n Hacer
        Escribir "Ingrese el valor para la posición ", i, ":"
        Leer vec[i]
    FinPara
    
    Escribir "El vector en orden inverso es:"
    Para i <- n Hasta 1 Con Paso -1 Hacer
        Escribir vec[i]
    FinPara
FinProceso