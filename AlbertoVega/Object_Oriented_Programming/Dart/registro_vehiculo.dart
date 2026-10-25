import "dart:io";

void main(){
  print("Bienvenido a AutoSpark, para poder empezar con el registro de cita para lavar su auto, ingrese a la del mismo a continuacion:");
  String? marca2 = stdin.readLineSync();
  print("Excelente, la marca registrada es ${marca2}, ahora por favor ingrese el color del vehiculo:");
  String? color2 = stdin.readLineSync();
  
}

class Auto{
  String? color;
  String? marca;
}