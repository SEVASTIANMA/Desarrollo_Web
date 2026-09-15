# Investigación: Método de Búsqueda Binaria

## 1. Definición
La **Búsqueda Binaria** es un algoritmo altamente eficiente para encontrar la posición de un elemento dentro de un vector que se encuentra previamente **ordenado**. Funciona bajo el principio de *divide y vencerás*, reduciendo progresivamente a la mitad el área de búsqueda en cada paso.

---

## 2. Lógica del Algoritmo
1. Se establecen dos punteros: `inicio` (posición 1) y `fin` (posición $N$).
2. Se calcula el punto medio del vector: $medio = \lfloor (inicio + fin) / 2 \rfloor$.
3. Se compara el valor en `vec[medio]` con el elemento buscado:
   * Si es igual, la búsqueda termina con éxito.
   * Si el elemento buscado es **menor**, se descarta la mitad derecha ajustando `fin = medio - 1`.
   * Si el elemento buscado es **mayor**, se descarta la mitad izquierda ajustando `inicio = medio + 1`.
4. El proceso se repite mientras `inicio <= fin`.

---

## 3. Ejemplo de Implementación (PSeInt)

```pseint
Proceso BusquedaBinaria
	Definir n, i, inicio, fin, medio, buscado Como Entero
	Definir encontrado Como Logico
	
	n <- 7
	Dimension vec[n]
	// El vector DEBE estar ordenado previamente
	vec[1]<-2; vec[2]<-5; vec[3]<-8; vec[4]<-12; vec[5]<-16; vec[6]<-23; vec[7]<-38
	
	Escribir "Ingrese el numero a buscar en el vector ordenado:"
	Leer buscado
	
	inicio <- 1
	fin <- n
	encontrado <- Falso
	
	Mientras inicio <= fin Y NO encontrado Hacer
		medio <- trunc((inicio + fin) / 2)
		
		Si vec[medio] = buscado Entonces
			encontrado <- Verdadero
		Sino
			Si buscado < vec[medio] Entonces
				fin <- medio - 1
			Sino
				inicio <- medio + 1
			FinSi
		FinSi
	FinMientras
	
	Escribir "---------------------------------------------"
	Si encontrado Entonces
		Escribir "El numero ", buscado, " se encuentra en la posicion: ", medio
	Sino
		Escribir "El numero ", buscado, " no se encuentra en el vector."
	FinSi
FinProceso
```

---

## 4. Cuadro Comparativo: Búsqueda Secuencial vs. Búsqueda Binaria

| Criterio | Búsqueda Secuencial | Búsqueda Binaria |
| :--- | :--- | :--- |
| **Requisito del Vector** | Funciona en vectores ordenados o desordenados. | **Requiere** que el vector esté obligatoriamente ordenado. |
| **Estrategia** | Revisa elemento por elemento de inicio a fin. | Divide el vector a la mitad en cada iteración. |
| **Rendimiento ($N$ alto)** | Lento para grandes volúmenes de datos. | Extremadamente rápido y optimizado. |
| **Estructura de Control** | Un ciclo `Para` simple. | Un ciclo `Mientras` con ajuste de límites. |

---

## 5. Análisis de Complejidad Temporal

* **Mejor Caso:** $O(1)$ — Ocurre cuando el elemento buscado se encuentra exactamente en la posición media en el primer intento.
* **Caso Promedio y Peor Caso:** $O(\log n)$ — Dado que el espacio de búsqueda se divide por la mitad en cada paso, el número máximo de comparaciones crece de forma logarítmica.

---

## 6. Conclusión
La búsqueda binaria es una de las herramientas más potentes en programación estructurada cuando se trabaja con colecciones de datos masivas. Aunque requiere el costo adicional de mantener el vector ordenado previa o dinámicamente, reduce drásticamente el número de comparaciones de un comportamiento lineal $O(n)$ a uno logarítmico $O(\log n)$.