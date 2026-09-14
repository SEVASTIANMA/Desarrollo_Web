# Investigación: Método de Ordenamiento por Selección (Selection Sort)

## 1. Definición
El **Ordenamiento por Selección** es un algoritmo de comparación sencillo que divide la lista en dos partes: una sublista de elementos ya ordenados y otra con los elementos pendientes por ordenar. En cada iteración, busca el elemento mínimo de la sublista no ordenada y lo intercambia con el primer elemento de dicha sublista.

---

## 2. Lógica del Algoritmo
1. Buscar el elemento más pequeño del vector.
2. Intercambiarlo con el elemento ubicado en la primera posición.
3. Buscar el segundo elemento más pequeño en el resto del vector.
4. Intercambiarlo con el elemento en la segunda posición.
5. Repetir el procedimiento desplazando el límite no ordenado hasta completar todo el vector.

---

## 3. Ejemplo de Implementation (PSeInt)

```pseint
Proceso OrdenamientoSeleccion
	Definir n, i, j, minPos, aux Como Entero
	n <- 5
	Dimension vec[n]
	vec[1]<-64; vec[2]<-25; vec[3]<-12; vec[4]<-22; vec[5]<-11
	
	Para i <- 1 Hasta n - 1 Hacer
		minPos <- i
		Para j <- i + 1 Hasta n Hacer
			Si vec[j] < vec[minPos] Entonces
				minPos <- j
			FinSi
		FinPara
		
		// Intercambio de posiciones
		aux <- vec[minPos]
		vec[minPos] <- vec[i]
		vec[i] <- aux
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Mínimo de Intercambios:** Realiza como máximo $n-1$ intercambios en total durante todo el proceso. | **Rendimiento Ineficiente:** Ejecuta siempre el número completo de comparaciones cuadráticas. |
| **Bajo Consumo de Memoria:** Algoritmo *in-place*, no requiere memoria adicional para ordenar. | **No Adaptativo:** Mantiene la misma complejidad sin importar si el vector ya está ordenado. |

---

## 5. Análisis de Complejidad Temporal

* **Mejor, Promedio y Peor Caso:** $O(n^2)$ — A diferencia de Burbuja o Inserción, Selección siempre realiza el número completo de comparaciones $\frac{n(n-1)}{2}$, independientemente del orden inicial del vector.

---

## 6. Conclusión
Selection Sort es ideal en escenarios donde las operaciones de escritura en memoria son costosas, ya que minimiza el número total de intercambios directos a un nivel lineal $O(n)$, aunque sus comparaciones sigan siendo cuadráticas.