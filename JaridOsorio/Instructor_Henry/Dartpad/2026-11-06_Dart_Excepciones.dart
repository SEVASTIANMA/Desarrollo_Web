// ==========================================
// Control de Errores con Try-Catch en Dart
// ==========================================

void main() {
  print('--- INICIO DE VALIDACIÓN ---');
  
  try {
    int resultado = dividir(10, 0);
    print('Resultado: $resultado');
  } catch (e) {
    print('❌ Error capturado: $e');
  } finally {
    print('🔄 Operación finalizada.');
  }
}

int dividir(int a, int b) {
  if (b == 0) {
    throw Exception('No es posible realizar una división entre cero.');
  }
  return a ~/ b;
}