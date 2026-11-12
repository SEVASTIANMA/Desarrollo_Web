// ==========================================
// Extension Methods en Dart
// ==========================================

void main() {
  String texto = "análisis y desarrollo de software";
  print('Texto original: $texto');
  print('Texto capitalizado: ${texto.capitalizar()}');
}

// Extensión para la clase String
extension StringExtension on String {
  String capitalizar() {
    if (this.isEmpty) return this;
    return this[0].toUpperCase() + this.substring(1);
  }
}