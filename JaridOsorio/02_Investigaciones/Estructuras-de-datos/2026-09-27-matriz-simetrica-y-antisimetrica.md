# Investigación: Matrices Simétricas y Antisimétricas

## 1. Definición
En álgebra lineal y programación estructurada, una **matriz simétrica** es una matriz cuadrada que es igual a su transpuesta ($A = A^T$). Por otro lado, una **matriz antisimétrica** es aquella cuya transpuesta es igual a su negativa ($A = -A^T$), lo que implica que todos los elementos de su diagonal principal deben ser cero.

---

## 2. Lógica de Verificación
1. **Simétrica:** Se verifica que para todo par de índices $i, j$, se cumpla $A[i, j] == A[j, i]$.
2. **Antisimétrica:** Se verifica que para la diagonal principal $A[i, i] == 0$ y para los demás elementos $A[i, j] == -A[j, i]$.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso VerificacionAntisimetrica
	Definir n, i, j Como Entero
	Definir esAnti Como Logico
	n <- 2
	Dimension mat[n, n]
	
	mat[1,1] <- 0;  mat[1,2] <- 4
	mat[2,1] <- -4; mat[2,2] <- 0
	
	esAnti <- Verdadero
	Para i <- 1 Hasta n Hacer
		Para j <- 1 Hasta n Hacer
			Si mat[i, j] <> -mat[j, i] Entonces
				esAnti <- Falso
			FinSi
		FinPara
	FinPara
	
	Si esAnti Entonces
		Escribir "La matriz es antisimétrica."
	FinSi
FinProceso
```

---

## 4. Cuadro Comparativo: Simétrica vs. Antisimétrica

| Criterio | Matriz Simétrica | Matriz Antisimétrica |
| :--- | :--- | :--- |
| **Condición Transpuesta** | $A = A^T$ | $A = -A^T$ |
| **Diagonal Principal** | Puede contener cualquier valor numérico. | **Obligatoriamente cero** ($A[i,i] = 0$). |
| **Relación de Espejo** | $A[i, j] = A[j, i]$ | $A[i, j] = -A[j, i]$ |

---

## 5. Análisis de Complejidad Temporal

* **Verificación Algorítmica:** $O(n^2)$ — Requiere iterar sobre las filas y columnas de la matriz cuadrada de orden $n$.

---

## 6. Conclusión
Comprender las propiedades de simetría en matrices permite optimizar espacio de almacenamiento en memoria, guardando únicamente la mitad superior o inferior de la estructura (matriz triangular) cuando se procesan grandes volúmenes de datos.