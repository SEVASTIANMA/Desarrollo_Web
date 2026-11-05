# Método Burbuja en PSeInt

## ¿Qué es el método burbuja?

El **método burbuja** es un algoritmo que sirve para **ordenar los elementos de un vector**.

Su funcionamiento consiste en **comparar dos elementos que están juntos**. Si están en el orden incorrecto, se intercambian.

Este proceso se repite varias veces hasta que todos los elementos quedan ordenados.

---

## ¿Cómo funciona?

Por ejemplo, tenemos el siguiente vector:

[5, 3, 8, 1, 2]

Primero comparamos `5` con `3`:

5 > 3

Como están desordenados, los intercambiamos:

[3, 5, 8, 1, 2]

Después comparamos `5` con `8`:

5 < 8

No se realiza ningún cambio.

Luego comparamos `8` con `1`:

8 > 1

Los intercambiamos:

[3, 5, 1, 8, 2]

Y continuamos comparando hasta recorrer todo el vector.

---

## Ejemplo en PSeInt

```pseint
Algoritmo MetodoBurbuja

    Definir vector, i, j, aux Como Entero
    Dimension vector[5]

    vector[1] <- 5
    vector[2] <- 3
    vector[3] <- 8
    vector[4] <- 1
    vector[5] <- 2

    Para i <- 1 Hasta 4 Hacer
        Para j <- 1 Hasta 5 - i Hacer

            Si vector[j] > vector[j + 1] Entonces
                aux <- vector[j]
                vector[j] <- vector[j + 1]
                vector[j + 1] <- aux
            FinSi

        FinPara
    FinPara

    Escribir "Vector ordenado:"

    Para i <- 1 Hasta 5 Hacer
        Escribir vector[i]
    FinPara

FinAlgoritmo 

## Resultado

El vector inicialmente es:

[5, 3, 8, 1, 2]

Después de aplicar el **método burbuja**, queda:

[1, 2, 3, 5, 8]

## ¿Qué hace la variable `aux`?

La variable `aux` sirve para **guardar temporalmente un valor durante el intercambio**.

Por ejemplo:

```text
aux <- vector[j]

vector[j] <- vector[j + 1]

vector[j + 1] <- aux