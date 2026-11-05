// ==========================================
// Creación de Funciones en Dart
// ==========================================

void main() {
  double num1 = 18.5;
  double num2 = 25.0;
  
  double resultado = calcularAreaRectangulo(num1, num2);
  print("El área calculada es: $resultado");
}

// Función con tipado de retorno
double calcularAreaRectangulo(double base, double altura) {
  return base * altura;
}