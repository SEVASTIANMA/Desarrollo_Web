# El Ciclo Para - Parte 1: Concepto y Utilidad

El **ciclo Para** (conocido formalmente como ciclo `for`) es una estructura de control cíclica que sirve para **repetir un bloque de código un número exacto de veces**. 

## ¿Para qué sirve principalmente?
* **Automatizar repeticiones:** Ejecuta la misma acción múltiples veces sin duplicar líneas de código.
* **Recorrer colecciones:** Permite leer, modificar o analizar elementos dentro de un arreglo, lista o matriz desde el principio hasta el final.
* **Controlar contadores:** Facilita la creación de secuencias numéricas (por ejemplo, contar de 1 a 100, o descender de 10 a 0).

## ¿Cuándo debes elegirlo?
Debes usar el ciclo **Para** cuando **conoces de antemano el número de iteraciones** (vueltas) que requiere el programa. Si el número de repeticiones depende de una condición externa que no sabes cuándo ocurrirá, es mejor usar un ciclo `Mientras` (While).
# El Ciclo Para - Parte 2: Estructura y Funcionamiento

Para que un ciclo Para funcione correctamente, necesita configurarse con **tres elementos esenciales** en una sola línea:

## Los 3 Componentes Clave
* **Variable de control (Inicio):** El punto de partida del ciclo (por ejemplo, `i = 1`).
* **Condición de límite (Fin):** El valor máximo o mínimo que detiene el ciclo (por ejemplo, `i <= 10`).
* **Paso (Incremento/Decremento):** Cuánto cambia la variable en cada vuelta (por ejemplo, avanzar de 1 en 1).

## Ejemplo Práctico (Pseudocódigo)
Imprimir los números pares del 2 al 10:

```psint
Para i <- 2 Hasta 10 Con Paso 2 Hacer
    Escribir "El número actual es: ", i
FinPara
```

### ¿Cómo se ejecuta internamente?
1. **Inicialización:** La variable `i` toma el valor de 2.
2. **Evaluación:** El sistema verifica si `i` (2) es menor o igual a 10. Como es verdadero, ejecuta el código interno.
3. **Paso:** Al terminar la vuelta, `i` aumenta en 2 (ahora vale 4).
4. **Repetición:** El proceso se repite hasta que `i` pasa a valer 12, rompiendo la condición de límite y finalizando el ciclo.
