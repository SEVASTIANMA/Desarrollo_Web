# Algoritmo Clasificador de Triángulos

Este algoritmo en PSeInt solicita al usuario las longitudes de tres lados, valida primero si es matemáticamente posible formar un triángulo con ellos (aplicando el teorema de la desigualdad triangular) y, en caso positivo, determina si es equilátero, isósceles o escaleno.

## Código Fuente (PSeInt)

```pseint
Algoritmo triangulo
    Definir la1 Como entero
    Definir la2 Como entero
    Definir la3 como entero
    
    Escribir 'Digite los 3 lados de su triangulo: '
    Leer la1, la2, la3
    
    // 1. Primero validamos si el triángulo realmente puede existir
    si la2 + la3 > la1 y la1 + la3 > la2 y la1 + la2 > la3 Entonces
        Escribir 'Es un triangulo!!'
        
        // 2. Si existe, procedemos a clasificarlo por sus lados
        si la1 = la2 y la2 = la3 Entonces
            Escribir 'Es un triangulo equilatero'
        SiNo
            si la1 = la2 o la1 = la3 o la3 = la2 Entonces
                Escribir 'Es un triangulo isosceles'
            SiNo
                Escribir 'Es un triangulo escaleno'
            FinSi
        FinSi
    SiNo
        Escribir 'No es un triangulo'
    FinSi
FinAlgoritmo
```

## Cómo funciona la lógica corregida

* **Estructura Anidada:** Al colocar la clasificación dentro de la validación, el programa nunca intentará adivinar el tipo de un triángulo imposible (evitando errores como decir que los lados 10, 2, 2 forman un triángulo isósceles).
* **Teorema de Existencia:** La condición la2 + la3 > la1 y la1 + la3 > la2 y la1 + la2 > la3 garantiza que la suma de dos lados cualesquiera sea estrictamente mayor que el lado restante.
