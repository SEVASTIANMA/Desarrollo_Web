import 'dart:io';

void main() {
  List<double> notas = List.generate(5, (i) {
    stdout.write('Nota ${i + 1}: ');
    return double.parse(stdin.readLineSync()!);
  });

  double promedio = notas.reduce((a, b) => a + b) / notas.length;
  print('Promedio: ${promedio.toStringAsFixed(2)}');