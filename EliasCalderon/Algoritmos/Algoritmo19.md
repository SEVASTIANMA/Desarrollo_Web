# Explicación del Algoritmo: promedioNotas

Este algoritmo en pseudocódigo calcula el **promedio de cuatro notas** de un estudiante y determina si **aprobó o no** la materia en función de su calificación final.

---

## Estructura y Funcionamiento Paso a Paso

### 1. Definición e Inicialización de Variables
El algoritmo comienza preparando el entorno de trabajo:
* **`Definir nota, suma, promedio Como Real`**: Crea variables para almacenar números con decimales.
* **`Definir i Como Entero`**: Crea una variable para controlar el ciclo de repetición.
* **`suma <- 0`**: Limpia la variable `suma` asignándole un valor inicial de cero para evitar errores en el cálculo.

### 2. Captura de Datos (Bucle `Para`)
El algoritmo ejecuta un ciclo repetitivo que se activa exactamente **4 veces** (desde `i <- 1` hasta `4` con paso `1`):
* Muestra en pantalla el mensaje: `"ingresar la nota: "`.
* Lee la calificación introducida por el usuario y la guarda en `nota`.
* Acumula el valor en la variable de control (`suma <- suma + nota`).

### 3. Cálculo del Promedio
Al terminar el ciclo de las 4 notas, realiza la operación matemática principal:
* **`promedio <- suma / 4`**: Divide la puntuación total acumulada entre el número de notas ingresadas.

### 4. Evaluación de la Condición y Resultados
El programa utiliza una estructura condicional (`si... Entonces... SiNo`) para validar el estado del estudiante:
* **Aprobado:** Si el promedio es **mayor o igual a 3.5** (`promedio >= 3.5`), el sistema imprime en pantalla el mensaje **'Aprobo'**.
* **Reprobado:** Si el promedio es inferior a 3.5, se ejecuta la alternativa y muestra **'No aprobo'**.

Finalmente, el algoritmo muestra el resultado numérico exacto mediante la instrucción:  
`Escribir 'El promedio es: ' promedio`.
