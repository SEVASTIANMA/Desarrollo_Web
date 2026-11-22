// ==========================================
// Null Safety y Operadores en Dart
// ==========================================

void main() {
  // Variable que puede aceptar valores nulos usando '?'
  String? nombreUsuario;
  
  // Operador de coalescencia nula '??'
  String usuarioFinal = nombreUsuario ?? "Invitado SENA";
  
  print("Usuario activo: $usuarioFinal");
  
  // Verificación de nulidad con funciones
  validarLongitud("Análisis y Desarrollo de Software");
}

void validarLongitud(String? texto) {
  // El operador '?.text' evita errores si el valor es nulo
  int? longitud = texto?.length;
  print("La longitud del texto es: $longitud caracteres.");
}