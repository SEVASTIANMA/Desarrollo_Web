Estructura Si Entonces en PSeInt

La estructura Si Entonces (condicional) permite ejecutar un bloque de instrucciones solo si se cumple una condición. Es la base de la toma de decisiones en programación.

Sintaxis básica
Si simple
Si condicion Entonces
    // instrucciones
FinSiS

Ejemplo 2: Si - SiNo
Algoritmo EjemploSiSiNo
Definir numero Como Entero

Escribir "Ingrese un numero: "
Leer numero

Si numero Mod 2 = 0 Entonces
    Escribir "El numero es par"
SiNo
    Escribir "El numero es impar"
FinSi
FinAlgoritmo