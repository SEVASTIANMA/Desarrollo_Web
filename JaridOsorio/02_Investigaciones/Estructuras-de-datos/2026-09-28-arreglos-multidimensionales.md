# Investigación: Arreglos Multidimensionales (N-Dimensiones)

## 1. Definición
Un **arreglo multidimensional** es una extensión de los vectores y matrices a $N$ dimensiones. Permite organizar la información en estructuras complejas como cubos de datos (3D) o hipercubos ($ND$), donde cada dimensión agrega un nuevo eje de acceso.

---

## 2. Representación Tridimensional (3D)
Para acceder a un elemento en un arreglo 3D se necesitan tres índices: `arreglo[capa, fila, columna]`. Esto permite representar tablas superpuestas en capas (por ejemplo, registros de ventas mensuales a lo largo de varios años).

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso ArregloTridimensional
	Definir capas, filas, cols, k, i, j Como Entero
	capas <- 2; filas <- 2; cols <- 2
	Dimension cubo[capas, filas, cols]
	
	// Llenado con 3 ciclos anidados
	Para k <- 1 Hasta capas Hacer
		Para i <- 1 Hasta filas Hacer
			Para j <- 1 Hasta cols Hacer
				cubo[k, i, j] <- k + i + j
			FinPara
		FinPara
	FinPara
FinProceso
```
---

## 4. Cuadro Comparativo: 1D vs. 2D vs. 3D

| Estructura | Dimensiones | Índices requeridos | Caso de Uso Común |
| :--- | :--- | :--- | :--- |
| **Vector** | 1D (Línea) | `vec[i]` | Listas simples de elementos. |
| **Matriz** | 2D (Plano) | `mat[i, j]` | Tablas, imágenes en escala de grises. |
| **Cubo** | 3D (Volumen) | `cubo[k, i, j]` | Imágenes a color (RGB), datos temporales. |

---

## 5. Análisis de Complejidad Temporal

* **Recorrido Completo (3D):** $O(n_1 \times n_2 \times n_3)$ — Requiere tres bucles anidados para procesar cada elemento del volumen.

---

## 6. Conclusión
El dominio de arreglos multidimensionales prepara al programador para trabajar con estructuras de datos complejas utilizadas en la industria, como procesamiento de video, simulaciones físicas y cubos OLAP en Big Data.