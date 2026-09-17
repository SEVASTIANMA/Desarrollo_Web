# Explicacion del Algoritmo: Division por Restas Sucesivas

Este algoritmo calcula el cociente y el residuo de una division entera utilizando unicamente operaciones de resta. Es el metodo logico basico que usan las computadoras cuando no tienen una operacion de division directa.

## Como funciona paso a paso

1. **Lectura de datos:** El programa solicita dos numeros enteros:
   * **A:** El dividendo (el numero que se va a dividir).
   * **B:** El divisor (el numero que divide).
2. **Inicializacion:** Se crea una variable llamada `cociente` y se establece en `0`. Esta variable contara cuantas veces cabe el divisor dentro del dividendo.
3. **El Ciclo de Restas (`mientras`):** El programa evalua si `A` es mayor o igual a `B`. Si se cumple la condicion:
   * Le resta el valor de `B` a `A` (va reduciendo el dividendo).
   * Le suma `1` al `cociente`.
   * Este proceso se repite en bucle hasta que `A` sea menor que `B`.
4. **Resultado final:** Cuando el ciclo termina porque `A` ya no se puede restar mas:
   * El valor acumulado en `cociente` es el resultado real de la division.
   * El valor que quedo atrapado en `A` es el residuo (lo que sobro).

---

## Ejemplo Practico (Prueba de Escritorio)

Si ingresamos A = 14 y B = 4:

* **Inicio:** `A = 14`, `B = 4`, `cociente = 0`
* **Vuelta 1:** 14 es mayor que 4 -> `A` pasa a ser 10 (14 - 4), `cociente` pasa a ser 1.
* **Vuelta 2:** 10 es mayor que 4 -> `A` pasa a ser 6 (10 - 4), `cociente` pasa a ser 2.
* **Vuelta 3:** 6 es mayor que 4 -> `A` pasa a ser 2 (6 - 4), `cociente` pasa a ser 3.
* **Termino:** ¿2 es mayor o igual que 4? No. El ciclo se detiene.

**Salida en pantalla:** `El cociente es 3 y el residuo es: 2`
