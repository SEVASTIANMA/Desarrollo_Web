# Investigación: Método de Ordenamiento Rápido (QuickSort)

## 1. Definición
**QuickSort** es un algoritmo de ordenamiento altamente eficiente basado en la técnica de *Divide y Vencerás*. Selecciona un elemento denominado **pivote** y reorganiza el arreglo de modo que los elementos menores al pivote queden a su izquierda y los mayores a su derecha.

---

## 2. Lógica del Algoritmo
1. Seleccionar un elemento pivote del arreglo.
2. Particionar el arreglo: mover los elementos menores que el pivote a su izquierda y los mayores a su derecha.
3. Aplicar recursivamente el mismo procedimiento a las dos sublistas generadas.

---

## 3. Ejemplo de Implementación Conceptualmente (PSeInt)

```pseint
// Esquema del particionado en QuickSort
Proceso ParticionadoPivote
	Definir n, i, pivote, aux, posPivote Como Entero
	n <- 5
	Dimension vec[n]
	vec[1]<-10; vec[2]<-80; vec[3]<-30; vec[4]<-90; vec[5]<-40
	
	pivote <- vec[5] // Seleccion del ultimo elemento como pivote
	Escribir "Pivote seleccionado: ", pivote
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Extremadamente veloz:** Excelente rendimiento promedio $O(n \log n)$. | **Recursividad:** Requiere memoria adicional en la pila de llamadas del sistema. |
| **In-place parcial:** No requiere duplicar el arreglo original en memoria. | **Inestable:** Puede alterar el orden relativo de elementos que posean el mismo valor. |

---

## 5. Análisis de Complejidad Temporal

* **Mejor y Caso Promedio:** $O(n \log n)$ — Ocurre cuando el pivote divide el arreglo en partes casi iguales de forma equilibrada.
* **Peor Caso:** $O(n^2)$ — Ocurre cuando el pivote seleccionado es el mayor o menor elemento de forma inconsistente (por ejemplo, en un arreglo ya ordenado).

---

## 6. Conclusión
QuickSort es uno de los algoritmos de ordenamiento más populares e importantes en la industria del software debido a su alta velocidad práctica y eficiencia en entornos reales de producción.