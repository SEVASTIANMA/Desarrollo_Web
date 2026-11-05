# Algoritmo: Organizador de Aprendices al Azar

Este algoritmo en PSeInt permite registrar a **26 estudiantes** y agruparlos automáticamente en **13 parejas aleatorias**, garantizando que nadie se repita ni quede sin compañero.

## Código Fuente (PSeInt)

```pseint
Algoritmo OrganizarAprendicesAlAzar
    Dimension aprendices
    Dimension elegido // Para saber quién ya fue emparejado
    
    // 1. Inicializar el control de elegidos en Falso
    Para i <- 1 Hasta 26 Con Paso 1 Hacer
        elegido[i] <- Falso
    FinPara
    
    // 2. Lectura de los nombres de los 26 aprendices
    Escribir "--- Registro de Aprendices ---"
    Para i <- 1 Hasta 26 Con Paso 1 Hacer
        Escribir "Ingrese el nombre del aprendiz ", i, ":"
        Leer aprendices[i]
    FinPara
    
    Escribir ""
    Escribir "--- Generando Parejas Aleatorias ---"
    Escribir ""
    
    // 3. Proceso para formar las 13 parejas
    Para pareja <- 1 Hasta 13 Con Paso 1 Hacer
        // Buscar el primer integrante al azar
        Repetir
            pos1 <- Azar(26) + 1 // Azar(26) da entre 0 y 25, sumamos 1
        Hasta Que elegido[pos1] = Falso
        elegido[pos1] <- Verdadero // Marcamos como seleccionado
        
        // Buscar el segundo integrante al azar
        Repetir
            pos2 <- Azar(26) + 1
        Hasta Que elegido[pos2] = Falso
        elegido[pos2] <- Verdadero // Marcamos como seleccionado
        
        // Mostrar la pareja conformada
        Escribir "Pareja ", pareja, ": ", aprendices[pos1], " y ", aprendices[pos2]
    FinPara
FinAlgoritmo
```

---

## Explicación del Funcionamiento

### 1. Control de Disponibilidad (Arreglos)
El programa utiliza dos listas (arreglos) de 26 posiciones:
* **`aprendices`**: Almacena los nombres de pila escritos por el usuario.
* **`elegido`**: Guarda valores lógicos (`Verdadero` o `Falso`). Actúa como una lista de asistencia para marcar quién ya tiene pareja y evitar duplicados.

### 2. Inicialización y Captura de Datos
* **Limpieza inicial:** El primer ciclo `Para` llena el arreglo `elegido` con el valor `Falso`. Esto le indica al sistema que, al arrancar, todos los estudiantes están disponibles.
* **Lectura:** El segundo ciclo solicita consecutivamente los 26 nombres y los almacena ordenadamente.

### 3. El Motor de Selección Aleatoria (`Repetir...Hasta Que`)
Para armar cada una de las 13 parejas, el algoritmo realiza dos búsquedas consecutivas bajo la misma lógica:
1. Genera un número aleatorio entre 1 y 26 mediante la instrucción `Azar(26) + 1`.
2. Evalúa la posición obtenida en el arreglo `elegido`.
3. **Si el estudiante ya fue seleccionado previamente** (`elegido[pos] = Verdadero`), el bucle `Repetir` se activa de nuevo y genera otro número.
4. **Si el estudiante está libre** (`elegido[pos] = Falso`), el bucle termina, se cambia su estado inmediatamente a `Verdadero` para "bloquearlo" y se añade a la pareja actual.
