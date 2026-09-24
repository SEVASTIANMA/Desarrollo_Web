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