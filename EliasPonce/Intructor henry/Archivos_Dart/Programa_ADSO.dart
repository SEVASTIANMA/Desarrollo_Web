void main() {
  // Lista de competencias del programa ADSO
  List<String> competencias = [
    'Análisis de requisitos',
    'Diseño de software',
    'Codificación en Python/Dart',
    'Pruebas unitarias'
  ];

  print('--- COMPETENCIAS ADSO ---');
  // Recorre e imprime cada elemento de la lista
  competencias.forEach((item) => print('• $item'));

  // Mapa (Clave-Valor) con información del proyecto
  Map<String, dynamic> proyecto = {
    'nombre': 'Sistema de Gestión Académica',
    'fase': 'Desarrollo',
    'integrantes': 3,
    'completado': false
  };

  print('\n--- ESTADO DEL PROYECTO ---');
  // Acceso a los valores del mapa usando sus claves
  print('Proyecto: ${proyecto['nombre']}');
  print('Fase actual: ${proyecto['fase']}');
}