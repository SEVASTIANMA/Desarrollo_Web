Proceso SumaYPromedioVector
    Definir n, i Como Entero
    Definir suma, promedio Como Real
    
    Escribir "Ingrese la cantidad de elementos del vector:"
    Leer n
    
    Dimension vec[n]
    suma <- 0
    
    Para i <- 1 Hasta n Hacer
        Escribir "Ingrese el valor para la posición ", i, ":"
        Leer vec[i]
        suma <- suma + vec[i]
    FinPara
    
    Si n > 0 Entonces
        promedio <- suma / n
        Escribir "La suma total de los elementos es: ", suma
        Escribir "El promedio de los elementos es: ", promedio
    Sino
        Escribir "La cantidad debe ser mayor a cero."
    FinSi
FinProceso