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
