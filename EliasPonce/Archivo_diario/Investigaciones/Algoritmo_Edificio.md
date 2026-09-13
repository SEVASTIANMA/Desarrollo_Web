# Algoritmo de Censo para Edificio de 10 Pisos - Parte 1: Estructura e Inicialización

Este bloque inicial del algoritmo se encarga de preparar todo el entorno de memoria y las variables necesarias para gestionar la información de los 10 niveles del edificio.

## Explicación de la Lógica y Componentes

*   **Definición de Arreglos (Vectores):** Se crean tres estructuras indexadas llamadas `mayoresPorPiso`, `menoresPorPiso` y `totalPorPiso`. Al dimensionarlas en 10, permiten almacenar de forma independiente los datos de cada planta sin perder los anteriores.
*   **Acumuladores Globales:** Variables destinadas a centralizar la suma de todo el edificio. Se inicializan explícitamente en `0` para evitar errores de cálculo por basura en memoria.

## Código PSeInt - Sección Inicial

```pseint
Algoritmo DetalleEdificio
    // 1. Declaración de estructuras para los 10 pisos (Vectores)
    Definir mayoresPorPiso, menoresPorPiso, totalPorPiso Como Entero
    Dimension mayoresPorPiso
    Dimension menoresPorPiso
    Dimension totalPorPiso
    
    // 2. Declaración de contadores y acumuladores globales
    Definir totalMayoresEdificio, totalMenoresEdificio, totalGeneralEdificio Como Entero
    Definir i Como Entero
    
    // 3. Inicialización manual de acumuladores del edificio
    totalMayoresEdificio <- 0
    totalMenoresEdificio <- 0
    totalGeneralEdificio <- 0
    
    Escribir "=================================================="
    Escribir "    CENSO DEL EDIFICIO (REGISTRO DE 10 PISOS)    "
    Escribir "=================================================="
    Escribir ""
```
# Algoritmo de Censo para Edificio de 10 Pisos - Parte 2: Entrada de Datos y Control

Esta sección ejecuta el núcleo operativo del programa: la recolección de datos de manera secuencial para cada piso a través de estructuras de control repetitivas.

## Explicación de la Lógica y Componentes

*   **Ciclo Para (For):** Gobierna el flujo general para repetir el proceso exactamente 10 veces, mapeando la variable contador `i` con el número de piso correspondiente.
*   **Estructura Repetir-Hasta Que (Do-While):** Funciona como un filtro de validación de datos. Si el usuario ingresa un número negativo de personas por error, el sistema detecta la anomalía, muestra una alerta y vuelve a exigir el número correcto hasta que este sea mayor o igual a cero.
*   **Cálculo Intermedio:** En cada iteración calcula la suma interna del piso actual y añade estos valores a los totales acumulados del edificio completo.

## Código PSeInt - Sección de Captura

```pseint
    // 4. Bucle principal para iterar piso por piso
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir "--- PISO ", i, " ---"
        
        // Control y validación para el ingreso de mayores de edad
        Repetir
            Escribir "Ingrese la cantidad de MAYORES de edad en este piso: "
            Leer mayoresPorPiso[i]
            Si mayoresPorPiso[i] < 0 Entonces
                Escribir "Error: La cantidad no puede ser negativa."
            FinSi
        Hasta Que mayoresPorPiso[i] >= 0
        
        // Control y validación para el ingreso de menores de edad
        Repetir
            Escribir "Ingrese la cantidad de MENORES de edad en este piso: "
            Leer menoresPorPiso[i]
            Si menoresPorPiso[i] < 0 Entonces
                Escribir "Error: La cantidad no puede ser negativa."
            FinSi
        Hasta Que menoresPorPiso[i] >= 0
        
        // Procesamiento matemático por cada ciclo
        totalPorPiso[i] <- mayoresPorPiso[i] + menoresPorPiso[i]
        
        // Actualización en tiempo real de los totales generales
        totalMayoresEdificio <- totalMayoresEdificio + mayoresPorPiso[i]
        totalMenoresEdificio <- totalMenoresEdificio + menoresPorPiso[i]
        totalGeneralEdificio <- totalGeneralEdificio + totalPorPiso[i]
        
        Escribir "Habitantes totales en el Piso ", i, ": ", totalPorPiso[i]
        Escribir "" 
    FinPara
```
