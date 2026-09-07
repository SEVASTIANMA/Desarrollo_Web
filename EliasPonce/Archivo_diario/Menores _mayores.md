Algoritmo ClasificarHabitantes
    Definir totalPersonas, edad, menores, mayores, i Como Entero
    
    Escribir "Ingrese la cantidad total de personas que viven en el edificio:"
    Leer totalPersonas
    
    // Inicializar los contadores
    menores <- 0
    mayores <- 0
    
    // Ciclo para registrar la edad de cada persona
    Para i <- 1 Hasta totalPersonas Con Paso 1 Hacer
        Escribir "Ingrese la edad de la persona número ", i, ":"
        Leer edad
        
        // Verificar si es mayor o menor de edad (tomando 18 años como mayoría de edad)
        Si edad >= 18 Entonces
            mayores <- mayores + 1
        Sino
            menores <- menores + 1
        FinSi
    FinPara
    
    // Mostrar los resultados finales
    Escribir "========================================="
    Escribir "Resultados del censo del edificio:"
    Escribir "Total de habitantes: ", totalPersonas
    Escribir "Cantidad de menores de edad: ", menores
    Escribir "Cantidad de mayores de edad: ", mayores
    Escribir "========================================="
FinAlgoritmo
