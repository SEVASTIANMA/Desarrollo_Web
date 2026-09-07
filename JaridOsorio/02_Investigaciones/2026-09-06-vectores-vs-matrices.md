# Investigación: Vectores (1D) vs. Matrices (2D)

## 1. Definición
Un **vector** (arreglo unidimensional) es una estructura de datos lineal que almacena elementos del mismo tipo organizados en una sola fila. Una **matriz** (arreglo bidimensional) expande este concepto a una cuadrícula formada por filas y columnas.

---

## 2. Cuadro Comparativo

| Criterio | Vectores (Unidimensionales) | Matrices (Bidimensionales) |
| :--- | :--- | :--- |
| **Dimensiones** | 1 Dimensión (Línea) | 2 Dimensiones (Tabla / Cuadrícula) |
| **Índices requeridos** | 1 índice (`vector[i]`) | 2 índices (`matriz[fila][columna]`) |
| **Ciclos para recorrer** | 1 ciclo simple (`Para`) | Ciclos anidados (`Para` dentro de otro `Para`) |
| **Casos de uso típicos** | Listas de notas, precios, inventarios | Tableros de juegos, imágenes, coordenadas |

---

## 3. Ejemplo Estructural en Pseudocódigo

```pseint
// Recorrido de Vector (1D)
Para i <- 1 Hasta 5 Hacer
    Escribir vector[i]
FinPara

// Recorrido de Matriz (2D)
Para f <- 1 Hasta 3 Hacer
    Para c <- 1 Hasta 3 Hacer
        Escribir matriz[f, c]
    FinPara
FinPara
```

---

## 4. Análisis de Uso

* **Vectores (1D):** Son la opción ideal cuando la información se puede procesar de forma lineal, secuencial o cronológica sin relaciones de tablas complejas (por ejemplo: listas de precios, registros de asistencia o arreglos de notas individuales).
* **Matrices (2D):** Resultan indispensables cuando los datos representan relaciones entre dos dimensiones (por ejemplo: cuadrículas de juegos como tres en raya, mapas de coordenadas, imágenes en escala de grises compuestas por píxeles o tablas de calificaciones por materia y estudiante).

---

## 5. Conclusión

La transición de vectores a matrices marca el paso fundamental desde el pensamiento algorítmico básico hacia la manipulación de estructuras de datos complejas. Mientras que los vectores nos permiten almacenar colecciones simples de datos, las matrices nos otorgan la capacidad de modelar escenarios del mundo real estructurados en tablas o cuadrículas. Dominar ambas estructuras y comprender cómo recorrerlas mediante ciclos simples o anidados es un pilar indispensable para avanzar hacia lenguajes de programación de alto nivel y el diseño de software estructurado.