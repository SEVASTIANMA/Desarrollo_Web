// ==========================================
// Clases y Constructores Nombrados en Dart
// ==========================================

void main() {
  ModuloFormativo modulo = ModuloFormativo(
    codigo: "ADSO-03",
    nombre: "Análisis y Diseño de Software",
    horasSemanales: 12,
  );

  modulo.resumen();
}

class ModuloFormativo {
  final String codigo;
  final String nombre;
  final int horasSemanales;

  ModuloFormativo({
    required this.codigo,
    required this.nombre,
    required this.horasSemanales,
  });

  void resumen() {
    print("Módulo [$codigo]: $nombre -$horasSemanales h/semana");
  }
}