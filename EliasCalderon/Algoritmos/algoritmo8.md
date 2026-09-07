Algoritmo TablaDelCinco
    Definir i, resultado Como Entero
    
    Escribir '==================================='
	Escribir '  A continuacion la tabla del 5 '
	Escribir '                                   '
	Escribir '==================================='
    
    Para i <- 1 Hasta 10 Hacer
        resultado <- 5 * i
        
        Si resultado > 10 Entonces
            Escribir "5 x ", i, " = ", resultado, "  �Es mayor que 10!  "
        Sino
            Escribir "5 x ", i, " = ", resultado
        FinSi
    FinPara
	
	Escribir '                         '
	Escribir '                         '
FinAlgoritmo



# Explicacion del Algoritmo: Tabla del Cinco

Este algoritmo esta escrito en PSeInt (pseudocodigo) y su objetivo principal es calcular y mostrar la tabla de multiplicar del numero 5, desde el 1 hasta el 10, aplicando una condicion especial a los resultados.

---

## Estructura y Funcionamiento Paso a Paso

### 1. Definicion de Variables
```pseudocode
Definir i, resultado Como Entero
```
* **i**: Funciona como el contador del bucle (multiplicador del 1 al 10).
* **resultado**: Almacena el valor de la multiplicacion en cada iteracion.

### 2. Encabezado Visual
El programa imprime en la consola un diseño decorativo para presentar el ejercicio de forma limpia.

### 3. El Bucle o Ciclo (Para)
```pseudocode
Para i <- 1 Hasta 10 Hacer
    resultado <- 5 * i
```
* El algoritmo repite el proceso 10 veces.
* En cada vuelta, multiplica el numero 5 por el valor actual de i y lo guarda en resultado.

### 4. Estructura Condicional (Si - Sino)
Aqui se evalua el valor obtenido para decidir que texto mostrar:

* **Si el resultado es mayor a 10** (desde 5 x 3 en adelante):
  Muestra la operacion y añade la alerta: ¡Es mayor que 10!.
* **Sino (si es 10 o menor)** (para 5 x 1 y 5 x 2):
  Muestra unicamente la operacion matematica estandar.

---

## Resultado Esperado en Consola

Al ejecutar el codigo, la salida final sera la siguiente:

```text
===================================
   A continuacion la tabla del 5   
                                   
===================================
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15 ¡Es mayor que 10! 
5 x 4 = 20 ¡Es mayor que 10! 
5 x 5 = 25 ¡Es mayor que 10! 
5 x 6 = 30 ¡Es mayor que 10! 
5 x 7 = 35 ¡Es mayor que 10! 
5 x 8 = 40 ¡Es mayor que 10! 
5 x 9 = 45 ¡Es mayor que 10! 
5 x 10 = 50 ¡Es mayor que 10! 
```
