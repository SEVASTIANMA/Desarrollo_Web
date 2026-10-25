import "dart:io";

void main(){
  print("Bienvenido a AutoSpark, para poder empezar con el registro de cita para lavar su auto, ingrese la marca del mismo a continuacion:");
  String? marca1 = stdin.readLineSync();
  print("Excelente, la marca registrada es ${marca1}, ahora por favor ingrese el color del vehiculo:");
  String? color1 = stdin.readLineSync();

  Auto auto = Auto(marca1, color1);

  print("Su auto ha sido registrado con exito. Carro ${auto.marca} de color ${auto.color}");
}

class Auto{
  String? color;
  String? marca;
  Auto(this.marca, this.color);
}