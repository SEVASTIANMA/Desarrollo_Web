# Explicación Paso a Paso: Algoritmo de Ordenamiento y Búsqueda en Vectores (PSeInt)

---

## 1. Preparación y Dimensionamiento (El inicio)
Antes de guardar cualquier dato, el programa necesita saber con qué espacio va a trabajar:
* **Entrada del tamaño (`n`):** Se le pide al usuario que indique cuántos números va a ingresar para no desperdiciar memoria ni recorrer casillas vacías.
* **Reserva de memoria (`Dimension`):** Se crea el vector indicando su capacidad máxima (por ejemplo, 50). Funciona como apartar un casillero con espacios numerados.

---

## 2. Llenado del Arreglo (El ingreso de datos)
Una vez definido el tamaño, se utiliza un bucle o ciclo `Para` repetitivo:
* El ciclo recorre las posiciones desde la `1` hasta la `n`.
* En cada vuelta, se le pide un número al usuario mediante un mensaje en pantalla y se guarda de inmediato en la posición actual del vector (`vector[i]`).

---

## 3. El Ordenamiento Burbuja (La parte más compleja)
Para ordenar los números de menor a mayor de forma automática, se utilizan **dos bucles `Para` anidados** (un ciclo dentro de otro):
* **El ciclo externo (`i`):** Controla cuántas pasadas completas se darán por todo el vector.
* **El ciclo interno (`j`):** Realiza las comparaciones de dos en dos (`vector[j]` con su vecino `vector[j + 1]`).
* **El intercambio (*Swap*):** Si el número de la izquierda es mayor que el de la derecha, significa que están desordenados. Para corregirlo sin perder ningún dato, se usa una variable temporal llamada `aux`:
  1. Se guarda el valor de la izquierda en `aux`.
  2. Se pasa el valor de la derecha a la posición de la izquierda.
  3. Se coloca el valor guardado en `aux` en la posición de la derecha.
  * *¿Por qué se llama burbuja?* Porque con cada pasada, el número más grande va "flotando" o desplazándose hacia el final del vector.

---

## 4. Visualización del Vector Ordenado
Terminado el proceso anterior, el vector ya se encuentra organizado de forma ascendente. Para que el usuario lo compruebe:
* Se vuelve a recorrer el vector con un ciclo `Para`.
* Se utiliza la instrucción `Escribir Sin Saltar` para imprimir los números uno al lado del otro entre corchetes (ej. `[2] [5] [12] [33]`), logrando una vista limpia en horizontal.

---

## 5. La Búsqueda Secuencial
Para encontrar un número específico dentro del vector ya ordenado:
* Se le pide al usuario que digite el número que desea buscar y se guarda en una variable (`buscar`).
* Se inicializan dos ayudas tácticas:
  * Una variable lógica llamada `encontrado` que arranca en `Falsa` (asumiendo que el número no está hasta demostrar lo contrario).
  * Una variable `pos` que arranca en `-1` para registrar la posición exacta si aparece.
* Se recorre todo el vector celda por celda comparando si el contenido es igual al valor buscado. Si la respuesta es **Sí**, se cambia `encontrado` a `Verdadero` y se guarda la posición (`pos <- i`).

---

## 6. El Resultado Final
Finalmente, se evalúan las banderas del paso anterior:
* Si `encontrado` terminó siendo `Verdadero`, se le muestra al usuario un mensaje de éxito con la posición exacta.
* Si terminó siendo `Falso`, se le avisa que el número no existe en el arreglo.

---

Algoritmo VectorOrdenamientoYBusqueda
    Definir n, i, j, aux, buscar, pos Como Entero
    Definir encontrado Como Logico
    
    Escribir "Ingrese la cantidad de elementos para el vector (máx. 50): "
    Leer n
    
    Dimension vector[50]
    
    // 1. Llenar el vector
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir "Ingrese el valor para la posición [", i, "]: "
        Leer vector[i]
    FinPara
    
    // 2. Ordenar el vector usando el método burbuja (Ascendente)
    Para i <- 1 Hasta n - 1 Con Paso 1 Hacer
        Para j <- 1 Hasta n - i Con Paso 1 Hacer
            Si vector[j] > vector[j + 1] Entonces
                aux <- vector[j]
                vector[j] <- vector[j + 1]
                vector[j + 1] <- aux
            FinSi
        FinPara
    FinPara
    
    // Mostrar vector ordenado
    Escribir "----------------------------------------"
    Escribir " Vector Ordenado (Ascendente):"
    Escribir "----------------------------------------"
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Escribir Sin Saltar "[", vector[i], "] "
    FinPara
    Escribir ""
    Escribir "----------------------------------------"
    
    // 3. Buscar un elemento en el vector
    Escribir "Ingrese el número que desea buscar: "
    Leer buscar
    
    encontrado <- Falso
    pos <- -1
    
    Para i <- 1 Hasta n Con Paso 1 Hacer
        Si vector[i] == buscar Entonces
            encontrado <- Verdadero
            pos <- i
        FinSi
    FinPara
    
    // Mostrar resultado de la búsqueda
    Si encontrado Entonces
        Escribir "¡Elemento encontrado! Está en la posición: ", pos
    SiNo
        Escribir "El elemento ingresado no se encuentra en el vector."
    FinSi
    Escribir "----------------------------------------"
    
FinAlgoritmo