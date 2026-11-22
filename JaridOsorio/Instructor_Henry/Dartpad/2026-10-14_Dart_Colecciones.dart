// ==========================================
// Listas y Mapas (Colecciones) en Dart
// ==========================================

void main() {
  // Lista de competencias del programa ADSO
  List<String> competencias = [
    'Análisis de requisitos',
    'Diseño de software',
    'Codificación en Python/Dart',
    'Pruebas unitarias'
  ];

  print('--- COMPETENCIAS ADSO ---');
  competencias.forEach((item) => print('• $item'));

  // Mapa (Clave-Valor) con información del proyecto
  Map<String, dynamic> proyecto = {
    'nombre': 'Sistema de Gestión Académica',
    'fase': 'Desarrollo',
    'integrantes': 3,
    'completado': false
  };

  print('\n--- ESTADO DEL PROYECTO ---');
  print('Proyecto: ${proyecto['nombre']}');
  print('Fase actual: ${proyecto['fase']}');
}