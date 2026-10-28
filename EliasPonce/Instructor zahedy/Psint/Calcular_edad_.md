# Calculadora de Año de Nacimiento en PSeInt

Este programa solicita la edad del usuario y determina su año de nacimiento basándose en el año actual (**2026**). Incluye una validación para saber si la persona ya cumplió años en el año en curso, garantizando un resultado exacto.

## Código en PSeInt

```pseint
Algoritmo CalcularAnioNacimiento
    // Definir las variables que vamos a utilizar
    Definir edad, anioActual, anioNacimiento Como Entero
    Definir yaCumplioAnios Como Caracter
    
    // Asignar el año actual fijado en 2026
    anioActual <- 2026
    
    // Solicitar la edad al usuario
    Escribir "Por favor, introduce tu edad:"
    Leer edad
    
    // Preguntar si ya cumplió años en el año en curso
    Escribir "¿Ya cumpliste años este año? (S/N):"
    Leer yaCumplioAnios
    
    // Calcular el año de nacimiento según la respuesta
    Si yaCumplioAnios = "S" O yaCumplioAnios = "s" Entonces
        anioNacimiento <- anioActual - edad
    Sino
        anioNacimiento <- anioActual - edad - 1
    FinSi
    
    // Mostrar el resultado en pantalla
    Escribir "Tienes ", edad, " años, por lo tanto naciste en el año: ", anioNacimiento
FinAlgoritmo
```

## Explicación del código

El programa funciona de forma secuencial a través de los siguientes pasos:

* **Definición de variables:** Se crean tres variables numéricas (`edad`, `anioActual`, `anioNacimiento`) y una de texto (`yaCumplioAnios`) para guardar las respuestas del usuario.
* **Captura de datos:** El algoritmo pide la edad y luego pregunta con un `S` (Sí) o `N` (No) se ya pasó su cumpleaños este año. Esto evita el típico error de cálculo por un año de diferencia.
* **Estructura condicional (`Si... Entonces`):** 
  * Si ya cumplió años, resta la edad directamente al año actual (`2026 - edad`).
  * Si no ha cumplido años, resta la edad y le quita un año adicional (`2026 - edad - 1`).
* **Salida de resultados:** Imprime en pantalla el mensaje final con el año de nacimiento exacto.
