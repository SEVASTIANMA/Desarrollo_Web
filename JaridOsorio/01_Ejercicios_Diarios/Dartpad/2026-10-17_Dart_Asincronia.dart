// ==========================================
// Programación Asíncrona en Dart
// ==========================================

void main() async {
  print('1. Iniciando consulta a la base de datos...');
  
  // Llamada a función asíncrona que simula una petición de red
  String datos = await obtenerDatosServidor();
  print('3. Respuesta recibida: $datos');
}

Future<String> obtenerDatosServidor() {
  // Simula un retraso de 2 segundos sin bloquear el programa
  return Future.delayed(
    Duration(seconds: 2), 
    () => 'Registros de aprendices SENA cargados exitosamente.'
  );
}