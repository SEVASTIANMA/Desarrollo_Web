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

