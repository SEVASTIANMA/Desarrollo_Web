# Investigación: Matrices Esparsas (Dispersas)

## 1. Definición
Una **matriz esparsa** o dispersa es aquella en la que la gran mayoría de sus elementos tienen un valor nulo o cero. En lugar de almacenar toda la estructura en memoria en un arreglo bidimensional convencional, se utilizan técnicas de compresión para registrar únicamente los elementos no nulos junto con sus posiciones.

---

## 2. Lógica y Representación
Para optimizar el uso de memoria RAM, una matriz esparsa se suele representar mediante tres arreglos unidimensionales (vectores) o una lista enlazada:
1. **Vector de Valores:** Almacena solo los datos diferentes de cero.
2. **Vector de Filas:** Guarda el índice de fila de cada valor.
3. **Vector de Columnas:** Guarda el índice de columna de cada valor.

---

## 3. Ejemplo de Representación (PSeInt)

```pseint
Proceso MatrizEsparsa
	Definir filas, columnas, i, j, contNoNulos Como Entero
	filas <- 3; columnas <- 3
	Dimension mat[filas, columnas]
	
	// Matriz con la mayoria de ceros
	mat[1,1]<-0; mat[1,2]<-0; mat[1,3]<-5
	mat[2,1]<-0; mat[2,2]<-0; mat[2,3]<-0
	mat[3,1]<-8; mat[3,2]<-0; mat[3,3]<-0
	
	contNoNulos <- 0
	Para i <- 1 Hasta filas Hacer
		Para j <- 1 Hasta columnas Hacer
			Si mat[i, j] <> 0 Entonces
				contNoNulos <- contNoNulos + 1
				Escribir "Valor no nulo encontrado: ", mat[i, j], " en Posicion [", i, ",", j, "]"
			FinSi
		FinPara
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Ahorro masivo de memoria:** No desperdicia espacio guardando valores cero. | **Mayor complejidad algorítmica:** Acceder a un elemento requiere búsquedas adicionales. |
| **Mayor velocidad en procesamiento:** Se operan únicamente los valores significativos. | **Inflexibilidad:** La inserción o modificación de datos requiere reorganizar estructuras. |

---

## 5. Análisis de Complejidad Temporal

* **Acceso Directo:** En una matriz estándar es $O(1)$, pero en una matriz esparsa comprimida puede subir a $O(k)$, donde $k$ es el número de elementos no nulos.
* **Espacio en Memoria:** Pasa de $O(m \times n)$ a $O(k)$, siendo enormemente eficiente cuando $k \ll (m \times n)$.

---

## 6. Conclusión
El concepto de matriz esparsa es clave en áreas como el procesado de imágenes, el aprendizaje automático (Machine Learning) y el cálculo científico, donde se manejan tablas de datos gigantescas compuestas casi en su totalidad por valores nulos.
