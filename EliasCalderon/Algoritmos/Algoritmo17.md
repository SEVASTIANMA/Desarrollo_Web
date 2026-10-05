### Explicación Paso a Paso

* **Definición de Variables**  
  `Definir num1 Como Entero` y `Definir num2 Como Entero` preparan el sistema para almacenar únicamente números sin decimales.

* **Captura de Datos**  
  `Leer num1` y `Leer num2` detienen la ejecución para que el usuario escriba los dos valores por teclado.

* **Evaluación de Condiciones (`Si - Entonces - Sino`)**  
  1. **Paso 1:** Evalúa `num1 = num2`. Si es verdadero, el flujo termina aquí mostrando *"Es el mismo digito"*.
  2. **Paso 2:** Si es falso, salta al `Sino` y evalúa `num1 > num2`. Si es verdadero, imprime que el primer número supera al segundo.
  3. **Paso 3:** Si ambas condiciones anteriores fallaron, el sistema ejecuta el último `Sino` por defecto, determinando que el segundo número es el mayor.
