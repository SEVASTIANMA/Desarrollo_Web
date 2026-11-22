// ==========================================
// Encapsulamiento y Getters/Setters en Dart
// ==========================================

void main() {
  Evaluacion evaluacion = Evaluacion("Modelado UML");
  evaluacion.nota = 4.6;
  print("Tema: ${evaluacion.tema} | Nota: ${evaluacion.nota} \vert{} Aprobada:${evaluacion.aprobada}");
}

class Evaluacion {
  final String tema;
  double _nota = 0.0;

  Evaluacion(this.tema);

  double get nota => _nota;

  set nota(double valor) {
    if (valor >= 0.0 && valor <= 5.0) {
      _nota = valor;
    } else {
      print("Nota fuera de rango (0.0 - 5.0).");
    }
  }

  bool get aprobada => _nota >= 3.5;
}