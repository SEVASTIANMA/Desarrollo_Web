# Investigación: Método de Ordenamiento Shell (Shell Sort)

* **Fecha:** 2026-09-01
* **Autor:** Jarid Osorio
* **Módulo:** Algoritmos y Estructuras de Datos / SENA

---

## 1. Introducción y Concepto
El método de ordenamiento **Shell Sort** (diseñado por Donald Shell en 1959) es un algoritmo de ordenamiento interno eficiente que funciona como una generalización del **ordenamiento por inserción directa**.

Su objetivo principal es reducir la cantidad de desplazamientos que realiza el algoritmo de inserción tradicional. Para lograrlo, realiza comparaciones e intercambios entre elementos que se encuentran separados por una distancia fija llamada **salto o brecha (*gap*)**.

---

## 2. Funcionamiento Paso a Paso

1. **Definir el salto (*gap*):** Se selecciona una distancia inicial entre los elementos a comparar (usualmente la mitad de la longitud del arreglo: `gap = n / 2`).
2. **Comparación e intercambio:** Se dividen los datos en sublistas según el *gap* actual y se aplica un ordenamiento por inserción en cada sublista.
3. **Reducción del salto:** Se reduce el valor del *gap* (por ejemplo, dividiéndolo a la mitad en cada paso: `gap = gap / 2`).
4. **Fase final:** El proceso se repite sucesivamente hasta que el *gap* sea igual a 1. En este punto, se ejecuta una inserción estándar pero sobre un arreglo que ya está casi completamente ordenado.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso MetodoShell
    Definir arreglo, n, i, j, gap, aux Como Entero
    n <- 6
    Dimension arreglo[6]
    
    // Arreglo desordenado
    arreglo[1] <- 35; arreglo[2] <- 14; arreglo[3] <- 9;
    arreglo[4] <- 68; arreglo[5] <- 19; arreglo[6] <- 4;
    
    // Algoritmo Shell Sort
    gap <- trunc(n / 2)
    Mientras gap > 0 Hacer
        Para i <- gap + 1 Hasta n Hacer
            aux <- arreglo[i]
            j <- i
            Mientras j > gap Y arreglo[j - gap] > aux Hacer
                arreglo[j] <- arreglo[j - gap]
                j <- j - gap
            FinMientras
            arreglo[j] <- aux
        FinPara
        gap <- trunc(gap / 2)
    FinMientras

    // Mostrar arreglo ordenado
    Para i <- 1 Hasta n Hacer
        Escribir "Posición ", i, ": ", arreglo[i]
    FinPara
FinProceso

```
---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Mayor velocidad:** Es mucho más rápido que algoritmos simples ($O(n^2)$) como Burbuja o Inserción básica. | **Complejidad variable:** Su rendimiento exacto depende mucho de la secuencia de *gaps* elegida. |
| **In-place:** No consume memoria extra significativa ya que modifica el arreglo original directamente. | **No es estable:** Puede alterar el orden relativo original de elementos que tengan claves de valor igual. |
| **Ideal para arreglos medianos:** Excelente rendimiento en conjuntos de datos de tamaño moderado. | **Superado por avanzados:** Algoritmos como QuickSort o MergeSort son más eficientes en volúmenes masivos de datos. |

---

## 5. Análisis de Complejidad Temporal

* **Mejor Caso:** $O(n \log n)$
* **Caso Promedio:** Depende del intervalo, típicamente entre $O(n^{1.25})$ y $O(n^{1.5})$
* **Peor Caso:** $O(n^2)$

---

## 6. Conclusión
El ordenamiento Shell es una herramienta fundamental en la optimización de algoritmos. Permite transformar un proceso de inserción lento en uno con rendimiento cercano a logarítmico simplemente reorganizando previamente los datos lejanos.