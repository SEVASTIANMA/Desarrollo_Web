# Investigación: Método de Ordenamiento por Inserción (Insertion Sort)

## 1. Definición
El **Ordenamiento por Inserción** es un algoritmo intuitivo que construye la lista ordenada final elemento por elemento. Funciona de manera similar a como la mayoría de personas ordenan las cartas en una baraja de mano.

---

## 2. Lógica del Algoritmo
1. Se asume que el primer elemento (`vec[1]`) ya está "ordenado".
2. Se toma el siguiente elemento (`clave`) y se compara hacia atrás con los elementos a su izquierda.
3. Se desplazan hacia la derecha todos los elementos mayores que la `clave`.
4. Se inserta la `clave` en la posición vacía resultante.
5. Se repite el proceso para todos los elementos del vector.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso OrdenamientoInsercion
	Definir n, i, j, clave Como Entero
	n <- 5
	Dimension vec[n]
	vec[1]<-12; vec[2]<-11; vec[3]<-13; vec[4]<-5; vec[5]<-6
	
	Para i <- 2 Hasta n Hacer
		clave <- vec[i]
		j <- i - 1
		
		Mientras j >= 1 Y vec[j] > clave Hacer
			vec[j + 1] <- vec[j]
			j <- j - 1
		FinMientras
		
		vec[j + 1] <- clave
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Alta eficiencia en datos pequeños:** Rápido y sencillo para listas de pocos elementos. | **Ineficiente a gran escala:** Su rendimiento cae drásticamente con conjuntos masivos. |
| **Adaptativo:** Muy eficiente si el arreglo ya está parcialmente ordenado. | **Uso intensivo de desplazamientos:** Realiza múltiples asignaciones por elemento. |

---

## 5. Análisis de Complejidad Temporal

* **Mejor Caso:** $O(n)$ — Ocurre cuando el arreglo entra completamente ordenado.
* **Caso Promedio y Peor Caso:** $O(n^2)$ — Ocurre con elementos distribuidos al azar o en orden inverso.

---

## 6. Conclusión
Insertion Sort es uno de los algoritmos más prácticos cuando se trata de conjuntos de datos pequeños o listas en las que constantemente se agregan elementos nuevos a un arreglo preordenado.