pila = []
print("--- Registro de Alumnos en Pila (Límite: suma edades < 100) ---")
edades = 0
while edades < 100:
    edad = int(input(f"\nEdad del alumno {len(pila) + 1}: "))
    estatura = float(input(f"Estatura del alumno {len(pila) + 1} (en m): "))
    pila.append((edad, estatura))
    edades += edad
alumnos = len(pila)
estaturas = mayores = altos = 0
while len(pila) > 0:
    alumno = pila.pop()
    estaturas += alumno[1]
    if alumno[0] > 18: 
        mayores += 1
    if alumno[1] > 1.75: 
        altos += 1
if alumnos > 0:
    print(f"Edad media: {(edades / alumnos):.2f} años")
    print(f"Estatura media: {(estaturas / alumnos):.2f} m")
    print(f"Alumnos mayores de 18: {mayores}")
    print(f"Alumnos de más de 1.75m: {altos}")
    
    
    '''
    # Explicación del Algoritmo de Registro de Alumnos

## Este algoritmo en Python realiza el **registro de datos de alumnos (edad y estatura) en una estructura de pila**, deteniendo la captura cuando la suma acumulada de las edades alcanza o supera los 100 años. Posteriormente, procesa los datos extrayéndolos de la pila para calcular y mostrar diversas estadísticas.

---

## ¿Qué hace paso a paso?

### 1. Fase de Registro (Primer ciclo `while`)
* Solicita de forma continua la **edad** y la **estatura** de cada alumno.
* Guarda los datos como una tupla `(edad, estatura)` y los agrega al final de la lista `pila` usando `.append()`.
* Acumula la edad ingresada en la variable `edades`.
* **Condición de parada:** El ciclo se repite mientras `edades < 100`. En el momento en que la suma de las edades es igual o mayor a 100, la captura se detiene. Esto significa que el último alumno ingresado es el que hace que se rompa el límite.

### 2. Fase de Procesamiento (Segundo ciclo `while`)
* Vacía la lista elemento por elemento utilizando `.pop()`. Al ser una **pila**, los datos se procesan en orden inverso al que fueron introducidos (el último en entrar es el primero en salir).
* Acumula las estaturas de todos los alumnos en la variable `estaturas`.
* Cuenta cuántos alumnos tienen una edad estrictamente mayor a 18 años.
* Cuenta cuántos alumnos tienen una estatura estrictamente mayor a 1.75 metros.

### 3. Fase de Resultados
Si se registró al menos un alumno, el programa calcula y muestra en pantalla:
* La edad media (promedio).
* La estatura media (promedio).
* La cantidad total de alumnos mayores de 18 años.
* La cantidad total de alumnos que miden más de 1.75 metros.

---

## Observación sobre el comportamiento del límite

El algoritmo incluye en las estadísticas finales al último alumno ingresado (el que hizo que la suma de edades igualara o superara los 100). Por lo tanto, el promedio de edad reflejará la suma total real obtenida (que puede ser mayor a 100) dividida entre el número total de alumnos capturados.
'''