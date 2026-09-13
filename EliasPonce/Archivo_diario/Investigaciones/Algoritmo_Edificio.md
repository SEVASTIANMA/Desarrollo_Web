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
# Algoritmo de Censo para Edificio de 10 Pisos - Parte 3: Reporte y Estadísticas

La última etapa del programa se enfoca en el procesamiento de salida, extrayendo la información guardada en los arreglos para desplegarla en un formato limpio y legible.

## Explicación de la Lógica y Componentes

*   **Renderizado de Tabla:** Utiliza un ciclo rápido para recorrer nuevamente las dimensiones de los arreglos ya llenos, imprimiendo los datos tabulados fila por fila (Piso por Piso).
*   **Impresión de Totales:** Expone las variables acumuladoras finales que resolvieron las métricas de todo el complejo habitacional.

## Código PSeInt - Sección de Cierre

```pseint
    // 5. Presentación del reporte estructurado en pantalla
    Escribir "=========================================================="
    Escribir "              REPORTE DETALLADO DEL EDIFICIO              "
    Escribir "=========================================================="
    Escribir "Piso | Mayores Edad | Menores Edad | Total del Piso"
    Escribir "----------------------------------------------------------"
    
    // Extracción secuencial de datos guardados en los vectores
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir "  ", i, "  |       ", mayoresPorPiso[i], "      |       ", menoresPorPiso[i], "      |       ", totalPorPiso[i]
    FinPara
    
    // 6. Entrega de métricas globales consolidadas
    Escribir "----------------------------------------------------------"
    Escribir "RESUMEN FINAL DE LA ESTRUCTURA:"
    Escribir ">> Total de mayores de edad en el edificio: ", totalMayoresEdificio
    Escribir ">> Total de menores de edad en el edificio: ", totalMenoresEdificio
    Escribir ">> Población total del edificio (10 pisos): ", totalGeneralEdificio
    Escribir "=========================================================="
FinAlgoritmo
```
# Guía Técnica: Funciones y Estructuras Utilizadas en el Algoritmo

Para construir este sistema de censo en PSeInt, se emplearon comandos nativos, estructuras de control y funciones lógicas específicas. A continuación, se detalla el rol de cada una dentro del programa:

## 1. Comandos de Asignación y Declaración
*   **Definir ... Como Entero:** Se utiliza para reservar espacio en la memoria del computador y especificar de forma estricta que las variables (como `i`, `totalGeneralEdificio`, etc.) solo almacenarán números enteros sin decimales.
*   **Dimension:** Es la palabra clave que transforma una variable común en un **Arreglo (o Vector)**. Al definir `Dimension mayoresPorPiso[10]`, le indicamos al programa que cree una lista indexada con 10 casillas consecutivas para guardar información de forma independiente.
*   **Operador de Asignación (<-):** Se usa para guardar un valor o el resultado de una operación matemática dentro de una variable. Por ejemplo: `totalMayoresEdificio <- 0`.

## 2. Estructuras de Control de Flujo (Ciclos)
*   **Para ... Hasta ... Con Paso 1 Hacer:** Es un bucle controlado por un contador (la variable `i`). Se utiliza para automatizar tareas repetitivas cuando conocemos el número exacto de iteraciones (en este caso, recorrer los 10 pisos del edificio del 1 al 10).
*   **Repetir ... Hasta Que:** Es una estructura de control de ciclos que se ejecuta al menos una vez (*Do-While*). En este algoritmo actúa como un **Mecanismo de Validación**. El código obliga al usuario a reintroducir los datos continuamente si ingresa un valor erróneo o negativo.

## 3. Comandos de Entrada y Salida (I/O)
*   **Escribir:** Función nativa utilizada para enviar mensajes de texto y desplegar los resultados de los cálculos directamente en la pantalla de la consola del usuario.
*   **Leer:** Función interactiva que detiene temporalmente la ejecución del programa para capturar el dato numérico que el usuario digita a través del teclado y almacenarlo instantáneamente dentro de una variable o posición de un vector (ej. `Leer mayoresPorPiso[i]`).

## 4. Operadores Aritméticos y Lógicos
*   **Operador Suma (+):** Realiza la adición de los datos ingresados para obtener los subtotales de cada planta y actualizar los contadores globales.
*   **Operador de Comparación (< y >=):** Utilizado dentro de las condiciones condicionales (`Si` y `Hasta Que`) para verificar de forma matemática si los números ingresados cumplen con la regla de ser positivos.
