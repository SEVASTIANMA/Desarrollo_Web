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

