// ==========================================
// Métodos Funcionales en Listas (Dart)
// ==========================================

void main() {
  List<int> calificaciones = [38, 45, 29, 50, 42, 31];

  print('--- CALIFICACIONES ORIGINALES ---');
  print(calificaciones);

  // Filtrar notas aprobatorias ( mayores o iguales a 35, simulando escala de 50)
  var aprobados = calificaciones.where((nota) => nota >= 35).toList();
  print('\n✅ Notas aprobatorias filtradas: $aprobados');

  // Transformar datos (ej. aplicar un factor o redondear)
  var notasAjustadas = calificaciones.map((nota) => nota + 2).toList();
  print('📈 Notas con estímulo aplicado: $notasAjustadas');
}