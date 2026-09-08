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
Estructura y Funcionamiento del Algoritmo en PSeIntPara entender cómo funciona el programa, podemos dividirlo en tres dimensiones esenciales: qué es, qué hace y qué componentes tiene.[ Llenar Arreglo (1-100) ] ──> [ Mezclar (Azar) ] ──> [ Mostrar Desordenado ] ──> [ Ordenar (Burbuja) ]
 ¿Qué ES el algoritmo?Es un programa lógico de ordenamiento y manipulación de estructuras de datos lineales (arreglos). 
Es un simulador de aleatorio: Utiliza funciones matemáticas para romper secuencias lógicas.
Es una implementación de ordenamiento clásico: Aplica el método Burbuja (Bubble Sort), uno de los pilares educativos de la programación.
Es un algoritmo determinista adaptado: Aunque genera un resultado visualmente caótico (desordenado), sigue una serie de pasos estrictos y repetibles por el procesador.
 ¿Qué HACE el algoritmo? (Flujo de Ejecución)El código ejecuta de forma secuencial cuatro tareas principales:Inicializa los datos: Crea una lista numerada perfectamente del 1 al 100.
 Genera entropía (Mezcla): Toma cada posición del arreglo y la intercambia con otra posición elegida al azar.
  Esto garantiza que ningún número se repita y ninguno se pierda.
  Muestra el caos: Imprime en la pantalla la lista modificada para que el usuario verifique el desorden.
  Restablece el orden: Compara los números adyacentes uno a uno.
   Si un número es mayor (o menor) que el siguiente, los intercambia de lugar. Repite este proceso hasta que la lista vuelve a quedar perfectamente ordenada.
    ¿Qué TIENE el algoritmo? (Componentes)El algoritmo se construye utilizando las siguientes estructuras y herramientas de PSeInt:
    Estructura de Almacenamiento:Dimensionar vector(100): Un arreglo o vector unidimensional con espacio exacto para 100 elementos.
    Variables de Control (i, j, auxiliar, posicionAleatoria):Definidas como Enteros para controlar los ciclos y almacenar los datos temporalmente durante los intercambios.
    Estructuras de Control Repetitivas:Ciclos Para: Utilizados para recorrer el vector de principio a fin de manera controlada.
    Estructuras de Control Condicionales:Condicional Si...Entonces: Evalúa si un número está fuera de su lugar ideal para autorizar el movimiento.
    Funciones Nativas:Azar(100): Genera un número entero aleatorio entre 0 y 99 para seleccionar los índices de mezcla.