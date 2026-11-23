// ==========================================
// Control de Excepciones en Dart
// ==========================================

void main() {
  print('--- INICIO DE VALIDACIÓN DE DATOS ---');
  
  try {
    procesarEdad("veinte"); // Esto lanzará un error intencional
  } catch (e) {
    print('❌ Excepción capturada: $e');
  } finally {
    print('🔄 Bloque finally ejecutado: Operación finalizada.');
  }
}

void procesarEdad(String entrada) {
  int edad = int.parse(entrada); // Lanzará FormatException si no es número
  print('Edad procesada: $edad años');
}