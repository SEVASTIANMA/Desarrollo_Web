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
