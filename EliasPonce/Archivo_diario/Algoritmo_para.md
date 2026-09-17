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
# El Ciclo Para - Parte 3: Ejercicio Resuelto

Para dominar el ciclo Para, lo mejor es ver un ejercicio práctico de la vida real: **calcular la suma de los primeros 5 números enteros** (1 + 2 + 3 + 4 + 5).

## El Desafío
Queremos que la computadora sume los números del 1 al 5 acumulando el resultado en una variable y que al final nos muestre el total (que debería ser 15).

## Solución en Pseudocódigo

```psint
Algoritmo SumarCincoNumeros
    Definir acumulador, i Como Entero
    acumulador <- 0  // Empezamos la suma en cero
    
    // El ciclo se repite exactamente 5 veces
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        acumulador <- acumulador + i  // Suma el valor actual de 'i'
    FinPara
    
    Escribir "La suma total del 1 al 5 es: ", acumulador
FinAlgoritmo
```

## Simulación paso a paso (Prueba de escritorio)

El ciclo funciona como una alcancía donde metemos monedas en cada vuelta:

* **Vuelta 1:** `i` vale 1. El acumulador pasa de 0 a **1** (0 + 1).
* **Vuelta 2:** `i` aumenta a 2. El acumulador pasa de 1 a **3** (1 + 2).
* **Vuelta 3:** `i` aumenta a 3. El acumulador pasa de 3 a **6** (3 + 3).
* **Vuelta 4:** `i` aumenta a 4. El acumulador pasa de 6 a **10** (6 + 4).
* **Vuelta 5:** `i` aumenta a 5. El acumulador pasa de 10 a **15** (10 + 5).

Al terminar la quinta vuelta, el ciclo detecta que el siguiente número es 6 (fuera del límite), se detiene y el programa imprime en pantalla el resultado final: **15**.
