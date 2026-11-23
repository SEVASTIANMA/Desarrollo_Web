void main() {
  String texto = "análisis y desarrollo de software";
  print('Texto original: $texto');
  print('Texto capitalizado: ${texto.capitalizar()}');
}

 
extension StringExtension on String {
  String capitalizar() {
    if (this.isEmpty) return this;
    return this[0].toUpperCase() + this.substring(1);
  }
}
