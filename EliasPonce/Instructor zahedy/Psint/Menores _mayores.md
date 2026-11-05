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
# Explicación del Algoritmo de Habitantes

Este documento detalla el funcionamiento del código en PSeInt para contar las personas mayores y menores de edad en un edificio.

## Estructura del Código

El algoritmo se divide en **cuatro partes principales**:

1. **Definición e Inicialización**
   * Se crean las variables necesarias (`totalPersonas`, `edad`, `menores`, `mayores`).
   * Los contadores de personas se configuran en `0` para empezar limpios.

2. **Captura del Total**
   * El programa solicita al usuario la cantidad total de habitantes.
   * Este dato es fundamental porque define el límite del ciclo de preguntas.

3. **Ciclo de Evaluación (Bucle Para)**
   * El programa se repite tantas veces como personas vivan en el edificio.
   * En cada repetición, pide una edad y ejecuta una estructura condicional `Si-Sino`:
     * **Si la edad es >= 18:** Aumenta el contador de mayores en 1.
     * **Sino (es menor a 18):** Aumenta el contador de menores en 1.

4. **Despliegue de Datos**
   * Una vez evaluados todos los habitantes, el sistema imprime el resumen final con los tres totales.

---

## Vista Rápida del Codigo

* **Inicio** -> ¿Cuántos viven? -> *Ciclo (Pregunta edad -> Clasifica)* -> **Fin** -> Muestra totales.
