## PYTHON

notas = []

for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Introduce la nota {i}: "))
            notas.append(nota)
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

promedio = sum(notas) / len(notas)
print(f"\nEl promedio de las 5 notas es: {round(promedio, 2)}")

## DART

import 'dart:io';

void main() {
  List<double> notas = [];
  
  for (int i = 1; i <= 5; i++) {
    while (true) {
      stdout.write('Introduce la nota $i: ');
      String? entrada = stdin.readLineSync();
      double? nota = double.tryParse(entrada ?? '');
      if (nota != null) {
        notas.add(nota);
        break;
      } else {
        print('Por favor, introduce un número válido.');
      }
    }
  }

  double suma = notas.reduce((a, b) => a + b);
  double promedio = suma / notas.length;
  print('\nEl promedio de las 5 notas es: ${promedio.toStringAsFixed(2)}');
}


## VISUAL BASE

Sub CalcularPromedioCincoNotas()
    Dim fila As Integer
    Dim suma As Double
    Dim nota As Double
    Dim promedio As Double
    Dim celdasConNota As Integer
    
    suma = 0
    celdasConNota = 0
    
    For fila = 1 To 5
        If IsNumeric(Cells(fila, 1).Value) And Cells(fila, 1).Value <> "" Then
            nota = CDbl(Cells(fila, 1).Value)
            suma = suma + nota
            celdasConNota = celdasConNota + 1
        End If
    Next fila
    
    If celdasConNota = 5 Then
        promedio = suma / 5
        Cells(1, 2).Value = promedio
        MsgBox "El promedio es: " & Round(promedio, 2), vbInformation, "Resultado"
    Else
        MsgBox "Por favor, asegúrate de llenar las celdas A1 hasta A5 con números.", vbExclamation, "Error"
    End If
End Sub




# Explicación de los Algoritmos para Calcular el Promedio de 5 Notas

A continuación se detalla el funcionamiento paso a paso de cada uno de los programas implementados.

---

## 1. Funcionamiento en Python

El script de Python está diseñado para ejecutarse en la terminal interactuando dinámicamente con el usuario mediante los siguientes pasos:

* **Inicialización:** Crea una lista vacía llamada `notas` donde se almacenarán los valores numéricos introducidos por el usuario.
* **Ciclo de control (`for`):** Configura un bucle que se repite exactamente 5 veces (del 1 al 5) para solicitar cada una de las calificaciones.
* **Validación de errores (`try-except`):** Implementa un bucle `while True` que no permite avanzar hasta que el usuario digite un número válido (`float`). Si el usuario ingresa letras o texto, captura el error (`ValueError`), muestra un mensaje de advertencia y vuelve a pedir el dato.
* **Procesamiento de datos:** Una vez obtenidas las 5 notas válidas, utiliza la función nativa `sum(notas)` para sumar todos los elementos del arreglo y la divide entre `len(notas)` (que devuelve la cantidad de elementos, es decir, 5) para obtener la media aritmética.
* **Salida:** Imprime el resultado final en la consola formateando el promedio a dos valores decimales con la función `round()`.

---

## 2. Funcionamiento en Dart

El programa en Dart sigue una lógica de consola estructurada y fuertemente tipada:

* **Importación de librerías:** Utiliza la librería nativa `dart:io` para habilitar el manejo de flujos de entrada y salida de datos (`stdin` y `stdout`).
* **Declaración del vector:** Define una lista explícita de números decimales (`List<double> notas`) para almacenar las calificaciones.
* **Captura de consola:** Mediante un bucle `for`, utiliza `stdin.readLineSync()` para capturar la entrada del teclado como una cadena de texto que puede ser nula (`String?`).
* **Conversión segura (`tryParse`):** Emplea el método `double.tryParse()` para intentar transformar la cadena de texto en un número flotante. Si la conversión es exitosa (el valor no es `null`), añade la nota al arreglo con `.add()` e interrumpe el bucle de validación; de lo contrario, exige una nueva entrada.
* **Reducción de datos:** Calcula la sumatoria total del arreglo aplicando el método `.reduce((a, b) => a + b)`, el cual combina de forma consecutiva todos los elementos del arreglo.
* **Cálculo y formateo:** Divide el total acumulado entre `notas.length` y despliega el promedio en pantalla forzando los dos dígitos decimales con `.toStringAsFixed(2)`.

---

## 3. Funcionamiento en VBA (Excel)

Esta macro automatiza la lectura y escritura directamente sobre las cuadrículas de la hoja de cálculo activa en Excel:

* **Declaración de variables:** Define explícitamente los tipos de datos necesarios (`Integer` para los índices de filas y `Double` para las operaciones con decimales) garantizando un uso óptimo de la memoria.
* **Escaneo de celdas:** Utiliza un bucle `For` que recorre verticalmente las filas de la 1 a la 5 en la columna 1 (Columna A).
* **Validación de celdas (`IsNumeric`):** Evalúa individualmente que cada celda de la celda `A1` hasta la `A5` no se encuentre vacía y contenga estrictamente un valor numérico. Si cumple las condiciones, convierte el valor a tipo doble (`CDbl`) y lo acumula en la variable `suma`.
* **Condición de seguridad:** Verifica que se hayan leído las 5 notas correctamente. Si falta algún número en el rango especificado, interrumpe el proceso y arroja una alerta en pantalla (`MsgBox`) notificando la anomalía.
* **Impresión de resultados:** Si todas las celdas son válidas, calcula el promedio dividiendo el acumulado entre 5, escribe automáticamente el resultado en la celda `B1` (`Cells(1, 2)`) y despliega un cuadro de diálogo informativo finalizando la macro.

