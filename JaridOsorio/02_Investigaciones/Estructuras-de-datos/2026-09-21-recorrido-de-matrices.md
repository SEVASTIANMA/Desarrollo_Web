# Investigación: Técnicas de Recorrido en Matrices (Filas vs. Columnas)

## 1. Definición
El **recorrido de una matriz** es el proceso de visitar secuencialmente cada uno de sus elementos. La forma en que se estructuran los ciclos anidados determina si la matriz se procesa **por filas** (recorrido horizontal) o **por columnas** (recorrido vertical), lo cual tiene un impacto directo en la lógica del programa y en el rendimiento de la memoria.

---

## 2. Lógica del Algoritmo
1. **Recorrido por Filas:** El ciclo externo itera sobre las filas ($i$) y el interno sobre las columnas ($j$). Se procesa toda la Fila 1, luego la Fila 2, y así sucesivamente.
2. **Recorrido por Columnas:** El ciclo externo itera sobre las columnas ($j$) y el interno sobre las filas ($i$). Se procesa toda la Columna 1, luego la Columna 2, etc.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso RecorridoFilasColumnas
	Definir i, j, filas, columnas Como Entero
	filas <- 2; columnas <- 3
	Dimension mat[filas, columnas]
	
	mat[1,1]<-10; mat[1,2]<-20; mat[1,3]<-30
	mat[2,1]<-40; mat[2,2]<-50; mat[2,3]<-60
	
	Escribir "--- RECORRIDO POR FILAS ---"
	Para i <- 1 Hasta filas Hacer
		Para j <- 1 Hasta columnas Hacer
			Escribir "Elemento [", i, ",", j, "]: ", mat[i, j]
		FinPara
	FinPara
	
	Escribir "--- RECORRIDO POR COLUMNAS ---"
	Para j <- 1 Hasta columnas Hacer
		Para i <- 1 Hasta filas Hacer
			Escribir "Elemento [", i, ",", j, "]: ", mat[i, j]
		FinPara
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Criterio | Recorrido por Filas | Recorrido por Columnas |
| :--- | :--- | :--- |
| **Uso de Memoria RAM** | Altamente eficiente (*Cache Friendly*), ya que los datos se guardan contiguos por filas. | Menos eficiente en lenguajes de alto nivel por saltos frecuentes de memoria. |
| **Aplicación Principal** | Lectura e impresión estándar de tablas y reportes. | Cálculo de totales por categoría, promedios verticales o procesamiento por columnas. |
| **Estructura** | Ciclo externo = Filas (`i`), Ciclo interno = Columnas (`j`). | Ciclo externo = Columnas (`j`), Ciclo interno = Filas (`i`). |

---

## 5. Análisis de Complejidad Temporal

* **Complejidad Temporal:** $O(m \times n)$ en ambos casos, dado que independientemente del orden de los ciclos, se deben visitar la totalidad de las $m$ filas y $n$ columnas.

---

## 6. Conclusión
Comprender la diferencia entre el recorrido por filas y por columnas es fundamental para optimizar el rendimiento de los algoritmos. Aunque en PSeInt ambos métodos tardan prácticamente lo mismo, en lenguajes como C, C++ o Java el recorrido por filas aprovecha la memoria caché del procesador, ofreciendo un rendimiento superior en matrices de gran tamaño.
