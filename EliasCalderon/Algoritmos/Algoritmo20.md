# Explicación del Algoritmo: Sumas Sucesivas

Este algoritmo sirve para **multiplicar dos números enteros positivos utilizando sumas sucesivas**. En lugar de usar el operador de multiplicación directo (`*`), el programa suma el primer número a sí mismo tantas veces como indique el segundo número (por ejemplo: 5 × 3 es lo mismo que sumar 5 + 5 + 5).

---

## Estructura y Funcionamiento Paso a Paso

### 1. Entrada de datos
```pseudocode
Escribir 'Digite sus numeros a calcular: ' 
Leer num1, num2
```
* **Qué hace:** Muestra un mensaje en pantalla y le pide al usuario que introduzca dos números. 
* **Variables:** Los valores ingresados se almacenan en las variables `num1` y `num2`.

### 2. Validación de los números (Filtro de seguridad)
```pseudocode
si num1 > 0 Y num2 > 0 Entonces
...
SiNo
    Escribir 'Los numeros deben ser mayores a 0'
FinSi
```
* **Qué hace:** Es una estructura condicional (`si-entonces-sino`). Verifica que **ambos números sean estrictamente mayores que cero**.
* **Resultado:** Si el usuario introduce un número negativo o un cero, el algoritmo salta directamente al bloque `SiNo` y muestra un mensaje de error.

### 3. Inicialización del acumulador
```pseudocode
resultado <- 0
```
* **Qué hace:** Crea una variable llamada `resultado` y la limpia poniéndola en `0`. Esta variable funcionará como un "contenedor" donde se irán sumando los valores.

### 4. Bucle de sumas (El núcleo del cálculo)
```pseudocode
para i <- 1 Hasta num2 Hacer
    resultado <- resultado + num1
FinPara
```
* **Qué hace:** Este es un bucle `Para` (ciclo *for*) que se repite exactamente la cantidad de veces que indique `num2`.
* **Proceso:** En cada vuelta del ciclo, toma el valor actual de `resultado`, le suma el valor de `num1` y vuelve a guardar el nuevo total en `resultado`.

### 5. Salida del resultado
```pseudocode
Escribir 'El producto es: ' resultado
```
* **Qué hace:** Una vez que el bucle termina todas sus repeticiones, el algoritmo muestra en pantalla el total acumulado, que equivale al producto de la multiplicación.

---

## Ejemplo Práctico (Prueba de Escritorio)

Si ingresamos **`num1 = 5`** y **`num2 = 3`** (Calculando $5 \times 3$):

1. **Validación:** ¿$5 > 0$ y $3 > 0$? **Sí**, el programa continúa.
2. **Inicio:** `resultado` empieza en `0`.
3. **Bucle `Para` (Se ejecutará 3 veces):**
   * **Vuelta 1:** `resultado` = 0 + 5 = **5**
   * **Vuelta 2:** `resultado` = 5 + 5 = **10**
   * **Vuelta 3:** `resultado` = 10 + 5 = **15**
4. **Fin:** El bucle termina y el programa imprime: *"El producto es: 15"*.
