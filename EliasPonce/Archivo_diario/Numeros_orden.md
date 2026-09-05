Algoritmo NumerosAscendentes
    Dimensionar vector(100)
    Definir i, j, auxiliar, posicionAleatoria Como Entero
    
    // 1. Llenar el vector con números del 1 al 100
    Para i <- 1 Hasta 100 Con Paso 1 Hacer
        vector(i) <- i
    FinPara
    
    // 2. Desordenar el vector de manera aleatoria
    Para i <- 1 Hasta 100 Con Paso 1 Hacer
        posicionAleatoria <- Azar(100) + 1
        // Intercambiar valores
        auxiliar <- vector(i)
        vector(i) <- vector(posicionAleatoria)
        vector(posicionAleatoria) <- auxiliar
    FinPara
    
    Escribir "--- NÚMEROS DESORDENADOS ---"
    Para i <- 1 Hasta 100 Con Paso 1 Hacer
        Escribir vector(i)
    FinPara
    
    // 3. Ordenar de manera ASCENDENTE (Método Burbuja)
    Para i <- 1 Hasta 99 Con Paso 1 Hacer
        Para j <- 1 Hasta 100 - i Con Paso 1 Hacer
            Si vector(j) > vector(j + 1) Entonces
                auxiliar <- vector(j)
                vector(j) <- vector(j + 1)
                vector(j + 1) <- auxiliar
            FinSi
        FinPara
    FinPara
    
    Escribir "--- NÚMEROS ORDENADOS ASCENDENTE ---"
    Para i <- 1 Hasta 100 Con Paso 1 Hacer
        Escribir vector(i)
    FinPara
FinAlgoritmo
