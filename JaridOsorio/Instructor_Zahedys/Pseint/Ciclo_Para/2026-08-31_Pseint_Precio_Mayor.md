Proceso MayorPrecioProductos
    Definir n, i Como Entero
    Definir precio, mayor Como Real
    
    Escribir "Ingrese la cantidad de productos:"
    Leer n
    
    Si n > 0 Entonces
        mayor <- 0
        
        Para i <- 1 Hasta n Hacer
            Escribir "Ingrese el precio del producto ", i, ":"
            Leer precio
            
            Si precio > mayor Entonces
                mayor <- precio
            FinSi
        FinPara
        
        Escribir "El precio mayor es: ", mayor
    Sino
        Escribir "La cantidad de productos debe ser mayor a cero."
    FinSi
FinProceso