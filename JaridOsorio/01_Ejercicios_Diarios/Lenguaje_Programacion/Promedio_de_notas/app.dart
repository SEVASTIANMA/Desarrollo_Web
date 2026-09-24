import 'dart:io';

void main() {

  // 1. Solicitar y leer cada nota por teclado
  stdout.write('Ingresa la nota 1: ');
  double nota1 = double.parse(stdin.readLineSync()!);

  stdout.write('Ingresa la nota 2: ');
  double nota2 = double.parse(stdin.readLineSync()!);

  stdout.write('Ingresa la nota 3: ');
  double nota3 = double.parse(stdin.readLineSync()!);

  stdout.write('Ingresa la nota 4: ');
  double nota4 = double.parse(stdin.readLineSync()!);

  stdout.write('Ingresa la nota 5: ');
  double nota5 = double.parse(stdin.readLineSync()!);

  // 2. Sumar las notas de manera secuencial
  double sumaNotas = nota1 + nota2 + nota3 + nota4 + nota5;

  // 3. Calcular el promedio dividiendo entre 5
  double promedio = sumaNotas / 5;

  // 4. Mostrar el resultado final
  print('\n----------------------------------------');
  print('El promedio final de las 5 notas es: $promedio');
  print('----------------------------------------');
}

//Cómo funciona: Utiliza la librería dart.io para capturar la entrada de texto por la consola con stdin.readLineSync().

//Proceso: Cada valor se convierte a número decimal con double.parse(). Las 5 notas se guardan en variables independientes (nota1 a nota5), se suman de forma directa y lineal, y el resultado se divide entre 5 para obtener el promedio.