void main() async {
  print('1. Iniciando consulta a la base de datos...');
  
 
  String datos = await obtenerDatosServidor();
  print('3. Respuesta recibida: $datos');
}

Future<String> obtenerDatosServidor() {
 
  return Future.delayed(
    Duration(seconds: 2), 
    () => 'Registros de aprendices SENA cargados exitosamente.'
  );
