Ciclos en PSeInt

Los ciclos (o bucles) son estructuras que permiten repetir un bloque de instrucciones varias veces, mientras se cumpla (o no) una condición. En PSeInt existen tres tipos principales: Mientras, Repetir y Para.

1. Ciclo Mientras (While)

Repite el bloque mientras la condición sea verdadera. La condición se evalúa antes de ejecutar el bloque, por lo que puede no ejecutarse ni una vez.

Mientras condicion Hacer
    // instrucciones
FinMientras 

Ejemplo:

Algoritmo EjemploMientras
Definir contador Como Entero
contador <- 1

Mientras contador <= 5 Hacer
    Escribir "Contador: ", contador
    contador <- contador + 1
FinMientras
FinAlgoritmo