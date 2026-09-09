# Investigación: Método de Ordenamiento por Burbuja (Bubble Sort)

## 1. Definición
El ordenamiento por burbuja es uno de los algoritmos más sencillos en ciencias de la computación. Funciona revisando repetidamente una lista de elementos, comparando pares adyacentes e intercambiándolos si están en el orden incorrecto.

## 2. Lógica del Algoritmo
1. Recorrer el vector desde la primera posición hasta la penúltima.
2. Comparar el elemento actual con el elemento siguiente (`vec[j] > vec[j+1]`).
3. Si el elemento actual es mayor, intercambiar sus valores mediante una variable auxiliar.
4. Repetir las pasadas hasta que en un recorrido completo no se realice ningún intercambio.

## 3. Ejemplo de Implementación (PSeInt)
```pseint
Proceso Burbuja
	Definir n, i, j, aux Como Entero
	n <- 5
	Dimension vec[n]
	vec[1]<-12; vec[2]<-5; vec[3]<-3; vec[4]<-8; vec[5]<-1
	
	Para i <- 1 Hasta n - 1 Hacer
		Para j <- 1 Hasta n - i Hacer
			Si vec[j] > vec[j+1] Entonces
				aux <- vec[j]
				vec[j] <- vec[j+1]
				vec[j+1] <- aux
			FinSi
		FinPara
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Simplicidad:** Es uno de los algoritmos más fáciles de entender e implementar. | **Bajo rendimiento:** Ineficiente al trabajar con grandes volúmenes de datos. |
| **In-place:** No requiere memoria adicional significativa para ordenar los elementos. | **Exceso de escrituras:** Realiza múltiples operaciones de intercambio innecesarias. |

---

## 5. Análisis de Complejidad Temporal

* **Mejor Caso:** $O(n)$ — Ocurre cuando el conjunto de datos ya se encuentra ordenado de origen.
* **Caso Promedio:** $O(n^2)$ — Requiere recorridos cuadráticos en distribuciones aleatorias.
* **Peor Caso:** $O(n^2)$ — Ocurre cuando los elementos están posicionados en orden totalmente inverso.

---

## 6. Conclusión
Aunque el algoritmo de ordenamiento por burbuja no se utiliza en entornos de producción profesional debido a su baja eficiencia con grandes volúmenes de datos, representa una herramienta pedagógica fundamental para comprender la lógica de manipulación de estructuras de datos y comparaciones iterativas.