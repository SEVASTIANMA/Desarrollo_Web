import 'dart:io';

void main() {
  print('Nota 1:'); double n1 = double.parse(stdin.readLineSync()!);
  print('Nota 2:'); double n2 = double.parse(stdin.readLineSync()!);
  print('Nota 3:'); double n3 = double.parse(stdin.readLineSync()!);
  print('Nota 4:'); double n4 = double.parse(stdin.readLineSync()!);
  print('Nota 5:'); double n5 = double.parse(stdin.readLineSync()!);

  double promedio = (n1 + n2 + n3 + n4 + n5) / 5;

  print('\nEl promedio final de las 5 notas es: $promedio');
}

