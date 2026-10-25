import "dart:io";

void main(){
  print('Bienvenido a CiruPet, por favor si quiere una cita a continuacion ingrese el nombre y edad de su mascota.');
  print('Nombre:');
  String? name = stdin.readLineSync();
  print('Edad:');
  String? text2 = stdin.readLineSync()!;
}

class Mascota{
  String? nombre;
  int? edad;
  Mascota(this.nombre, this.edad);
}