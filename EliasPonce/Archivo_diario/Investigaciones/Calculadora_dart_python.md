# Calculadora Multilenguaje (Python y Dart)

Este documento contiene la implementacion de una calculadora basica en Python y Dart. Cada version incluye soporte para operaciones aritmeticas fundamentales: suma, resta, multiplicacion y division (con validacion para evitar errores de division por cero).

---

## Parte 1: Implementacion en Python

Python destaca por su sintaxis limpia y su facilidad para leer codigo. Utilizaremos funciones y un bucle while para mantener la calculadora activa.

### Codigo en Python

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def calculadora():
    print("--- Calculadora en Python ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        opcion = input("\nSelecciona una opcion (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer numero: "))
                num2 = float(input("Ingresa el segundo numero: "))
            except ValueError:
                print("Por favor, ingresa solo numeros validos.")
                continue

            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {dividir(num1, num2)}")
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
```

### Explicacion del Algoritmo (Python)

1. Funciones Core: Se definen cuatro funciones (sumar, restar, multiplicar, dividir) que encapsulan la logica matematica basica.
2. Control de Errores: En la funcion dividir, se evalua si el denominador es 0 mediante un condicional if para prevenir que el programa falle por un ZeroDivisionError.
3. Bucle de Ejecucion: Un ciclo while True mantiene el menu activo para que el usuario pueda hacer multiples calculos consecutivos.
4. Manejo de Excepciones: Se incluye un bloque try-except ValueError para capturar casos donde el usuario introduzca texto en lugar de numeros, evitando que la consola se cierre abruptamente.

---

## Parte 2: Implementacion en Dart

Dart es un lenguaje fuertemente tipado que se utiliza principalmente con Flutter. Su estructura requiere definir tipos de datos explicitos (double, String) y un punto de entrada obligatorio llamado main().

### Codigo en Dart

```dart
import 'dart:io';

double sumar(double a, double b) => a + b;
double restar(double a, double b) => a - b;
double multiplicar(double a, double b) => a * b;

dynamic dividir(double a, double b) {
  if (b == 0) {
    return "Error: No se puede dividir entre cero.";
  }
  return a / b;
}

void main() {
  print("--- Calculadora en Dart ---");
  print("1. Sumar");
  print("2. Restar");
  print("3. Multiplicar");
  print("4. Dividir");
  print("5. Salir");

  while (true) {
    stdout.write("\nSelecciona una opcion (1-5): ");
    String? opcion = stdin.readLineSync();

    if (opcion == '5') {
      print("¡Hasta luego!");
      break;
    }

    if (opcion == '1' || opcion == '2' || opcion == '3' || opcion == '4') {
      stdout.write("Ingresa el primer numero: ");
      double? num1 = double.tryParse(stdin.readLineSync() ?? '');

      stdout.write("Ingresa el segundo numero: ");
      double? num2 = double.tryParse(stdin.readLineSync() ?? '');

      if (num1 == null || num2 == null) {
        print("Por favor, ingresa solo numeros validos.");
        continue;
      }

      switch (opcion) {
        case '1':
          print("Resultado: \$num1 + num2 = {sumar(num1, num2)}");
          break;
        case '2':
          print("Resultado: \$num1 - num2 = {restar(num1, num2)}");
          break;
        case '3':
          print("Resultado: \$num1 * num2 = {multiplicar(num1, num2)}");
          break;
        case '4':
          var resultado = dividir(num1, num2);
          if (resultado is String) {
            print(resultado);
          } else {
            print("Resultado: \$num1 / num2 = resultado");
          }
          break;
      }
    } else {
      print("Opcion no valida. Intenta de nuevo.");
    }
  }
}
```

### Explicacion del Algoritmo (Dart)

1. Libreria de I/O: Importamos dart:io para poder utilizar stdin.readLineSync() y stdout.write(), necesarios para interactuar con la terminal.
2. Tipado Estricto: A diferencia de Python, aqui las funciones especifican que reciben y retornan valores tipo double. La funcion dividir usa el tipo dynamic porque puede devolver una cadena de texto (error) o un numero.
3. Manejo de Nulos (Null Safety): Usamos double.tryParse() junto con operadores de coalescencia nula (?? '') para convertir las entradas de texto a numero de forma segura. Si el usuario escribe algo invalido, el sistema asigna null y el programa le pide corregirlo sin crasear.
4. Estructura Control Switch: Reemplazamos la cadena de if-elif de Python por un bloque switch-case en Dart, lo cual es una practica mas eficiente y limpia para menus fijos.
