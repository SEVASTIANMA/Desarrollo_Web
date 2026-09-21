# Investigación: Introducción a Arreglos Bidimensionales (Matrices)

## 1. Definición
Una **matriz** o arreglo bidimensional es una estructura de datos que organiza información en una tabla compuesta por filas ($m$) y columnas ($n$). A diferencia de los vectores (unidimensionales), requiere dos índices para acceder a cualquier posición: `matriz[fila, columna]`.

---

## 2. Lógica y Estructura
Para manipular una matriz se utilizan **ciclos anidados**. El ciclo externo controla el recorrido de las filas, mientras que el ciclo interno recorre las columnas de cada fila.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso LlenarMostrarMatriz
	Definir f, c, filas, columnas Como Entero
	filas <- 3
	columnas <- 3
	Dimension mat[filas, columnas]
	
	// Llenado de la matriz
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir "Ingrese valor para [", f, ",", c, "]:"
			Leer mat[f, c]
		FinPara
	FinPara
	
	// Impresion de la matriz
	Escribir "--- CONTENIDO DE LA MATRIZ ---"
	Para f <- 1 Hasta filas Hacer
		Para c <- 1 Hasta columnas Hacer
			Escribir Sin Saltar mat[f, c], " "
		FinPara
		Escribir "" // Salto de linea por fila
	FinPara
FinProceso
```

---

## 4. Cuadro Comparativo: Ventajas vs. Desventajas

| Ventajas | Desventajas |
| :--- | :--- |
| **Representación espacial:** Permite modelar tablas, imágenes y mapas de forma intuitiva. | **Mayor complejidad:** Requiere lógica con ciclos anidados ($O(n^2)$). |
| **Acceso directo:** Permite consultar cualquier celda mediante sus dos coordenadas. | **Tamaño fijo:** Requiere definir sus dimensiones de forma estática en PSeInt. |

---

## 5. Análisis de Complejidad Temporal

* **Recorrido Completo:** $O(m \times n)$ — Se debe iterar sobre cada una de las $m$ filas y $n$ columnas para procesar la totalidad de celdas de la matriz.

---

## 6. Conclusión
Las matrices son fundamentales en programación para pasar del procesamiento de datos en secuencia simple a la manipulación de información estructurada en dos dimensiones.