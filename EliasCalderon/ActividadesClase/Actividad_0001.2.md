## PYTHON

Algoritmo PromedioSencillo
	Escribir "Introduce la nota 1:"
	Leer nota1
	Escribir "Introduce la nota 2:"
	Leer nota2
	Escribir "Introduce la nota 3:"
	Leer nota3
	Escribir "Introduce la nota 4:"
	Leer nota4
	Escribir "Introduce la nota 5:"
	Leer nota5
	
	promedio <- (nota1 + nota2 + nota3 + nota4 + nota5) / 5
	
	Escribir "El promedio es: ", promedio
FinAlgoritmo


## DART
import 'dart:io';

void main() {
  print('Introduce la nota 1:');
  String entrada1 = stdin.readLineSync() ?? '0';
  int nota1 = int.parse(entrada1);

  print('Introduce la nota 2:');
  String entrada2 = stdin.readLineSync() ?? '0';
  int nota2 = int.parse(entrada2);

  print('Introduce la nota 3:');
  String entrada3 = stdin.readLineSync() ?? '0';
  int nota3 = int.parse(entrada3);

  print('Introduce la nota 4:');
  String entrada4 = stdin.readLineSync() ?? '0';
  int nota4 = int.parse(entrada4);

  print('Introduce la nota 5:');
  String entrada5 = stdin.readLineSync() ?? '0';
  int nota5 = int.parse(entrada5);

  double promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5;

  print('El promedio es: $promedio');
  
}

## VISUAL BASE

Sub CalcularPromedioSencillo()
    Dim nota1 As Double
    Dim nota2 As Double
    Dim nota3 As Double
    Dim nota4 As Double
    Dim nota5 As Double
    Dim promedio As Double
    
    nota1 = Cells(1, 1).Value
    nota2 = Cells(2, 1).Value
    nota3 = Cells(3, 1).Value
    nota4 = Cells(4, 1).Value
    nota5 = Cells(5, 1).Value
    
    promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
    
    Cells(1, 2).Value = promedio
End Sub


# Explicación de los Algoritmos Secuenciales (Versión Sencilla)

A continuación se detalla el funcionamiento paso a paso de cada uno de los programas en su formato más básico y directo.

---

## 1. Funcionamiento en Python

Este programa interactúa con el usuario a través de la consola mediante un flujo lineal:

* **Captura de datos:** Solicita de forma consecutiva las 5 calificaciones. Utiliza la función `input()` para recibir el texto del teclado y `float()` para transformarlo inmediatamente en un número decimal.
* **Asignación:** Guarda cada calificación en una variable única e independiente (`nota1`, `nota2`, etc.).
* **Cálculo matemático:** Suma las 5 variables dentro de un paréntesis para obligar al sistema a realizar la suma primero, y luego divide el resultado de forma directa entre `5`.
* **Salida:** Muestra el promedio final en la pantalla utilizando la función `round(promedio, 2)` para recortar el resultado a solo dos decimales.

---

## 2. Funcionamiento en Dart

Esta versión utiliza una estructura limpia y fácil de comprender, evitando configuraciones complejas:

* **Lectura de texto (`String`):** El programa despliega un mensaje en pantalla y espera a que el usuario escriba. Lo que el usuario digita se guarda temporalmente como texto en variables llamadas `entrada`.
* **Seguridad contra vacíos (`?? '0'`):** Es un operador de control. Si por error el usuario presiona "Enter" sin escribir nada, el programa automáticamente asigna un texto `'0'` para evitar que el sistema se detenga o falle.
* **Conversión a número (`int.parse`):** Transforma el texto guardado en la `entrada` en un número entero real para poder realizar operaciones matemáticas con él.
* **Promedio:** Suma los 5 números enteros. Al dividirlos con la barra diagonal `/`, Dart calcula automáticamente el resultado con sus decimales correspondientes y lo muestra en la consola.

---

## 3. Funcionamiento en VBA (Excel)

Esta macro automatiza la lectura y el cálculo operando directamente sobre las cuadrículas de la hoja de Excel:

* **Declaración:** Define 6 variables de tipo `Double` (números con decimales) para almacenar las notas individuales y el resultado final.
* **Lectura de celdas (`Cells`):** El comando `Cells(fila, columna).Value` extrae el valor depositado en la hoja de cálculo. Lee verticalmente desde la celda `A1` (fila 1, columna 1) hasta la `A5` (fila 5, columna 1) y asigna cada valor a su variable correspondiente.
* **Procesamiento:** Ejecuta la fórmula matemática del promedio combinando las 5 variables y dividiéndolas entre 5.
* **Escritura:** Coloca el resultado final directamente en la celda `B1` (`Cells(1, 2)` representa fila 1, columna 2).

---

## 4. Funcionamiento en PSeInt

Es el algoritmo en pseudocódigo puro, estructurado de forma secuencial:

* **Instrucción `Escribir`:** Muestra un mensaje en la pantalla indicándole al usuario qué nota debe ingresar.
* **Instrucción `Leer`:** Pausa la ejecución del programa y espera a que el usuario teclee el número, guardándolo inmediatamente en la variable asignada.
* **Asignación (`<-`):** Suma las 5 variables, divide el total entre 5 y el resultado se almacena en la variable `promedio`.
* **Despliegue:** Imprime en la pantalla el mensaje final junto con el valor calculado.
