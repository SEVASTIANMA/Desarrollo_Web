// ==========================================
// Introducción a Streams en Dart
// ==========================================

import 'dart:async';

void main() {
  print('--- INICIO DEL FLUJO DE DATOS (STREAM) ---');
  
  // Crear un Stream que emite números enteros cada segundo
  Stream<int> contadorStream = Stream.periodic(Duration(seconds: 1), (val) => val + 1).take(3);

  // Escuchar el Stream (Programación Reactiva)
  contadorStream.listen((evento) {
    print('Datos recibidos del servidor: $evento');
  }, onDone: () {
    print('--- FLUJO FINALIZADO EXITOSAMENTE ---');
  });
}