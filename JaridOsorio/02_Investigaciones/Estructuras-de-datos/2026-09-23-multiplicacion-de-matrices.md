# Investigación: Multiplicación de Matrices

## 1. Definición
La **multiplicación de matrices** es una operación fundamental en álgebra lineal y computación. A diferencia de la suma, no se realiza elemento a elemento, sino multiplicando las filas de la primera matriz por las columnas de la segunda (*producto punto*).

---

## 2. Condición de Existencia
Para multiplicar dos matrices $A$ y $B$ ($A \times B$), el número de **columnas** de $A$ debe ser estrictamente igual al número de **filas** de $B$. Si $A$ es de dimensión $m \times n$ y $B$ es de $n \times p$, la matriz resultante $C$ tendrá dimensión $m \times p$.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso MultiplicacionMatrices
	Definir i, j, k, A, B, C Como Entero
	Dimension A[2, 2], B[2, 2], C[2, 2]
	
	A[1,1]<-1; A[1,2]<-2; A[2,1]<-3; A[2,2]<-4
	B[1,1]<-5; B[1,2]<-6; B[2,1]<-7; B[2,2]<-8
	
	Para i <- 1 Hasta 2 Hacer
		Para j <- 1 Hasta 2 Hacer
			C[i, j] <- 0
			Para k <- 1 Hasta 2 Hacer
				C[i, j] <- C[i, j] + (A[i, k] * B[k, j])
			FinPara
		FinPara
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Suma vs. Multiplicación de Matrices

| Criterio | Suma de Matrices | Multiplicación de Matrices |
| :--- | :--- | :--- |
| **Requisito Dimensional** | Ambas matrices deben ser de igual dimensión ($m \times n$). | Columnas de $A$ deben igualar a filas de $B$. |
| **Complejidad Algorítmica** | Se realiza en tiempo $O(m \times n)$ con 2 ciclos anidados. | Requiere 3 ciclos anidados, logrando una complejidad de $O(n^3)$. |
| **Propiedad Conmutativa** | Es conmutativa ($A + B = B + A$). | **No es conmutativa** ($A \times B \neq B \times A$). |

---

## 5. Análisis de Complejidad Temporal

* **Algoritmo Tradicional:** $O(n^3)$ — Requiere tres bucles anidados para calcular los productos y sumas acumuladas.
* **Algoritmos Optimizados (ej. Strassen):** Logran reducir la complejidad a aproximadamente $O(n^{2.81})$.

---

## 6. Conclusión
La multiplicación de matrices es el motor matemático detrás de gráficos 3D, videojuegos, procesamiento de imágenes y redes neuronales en inteligencia artificial.