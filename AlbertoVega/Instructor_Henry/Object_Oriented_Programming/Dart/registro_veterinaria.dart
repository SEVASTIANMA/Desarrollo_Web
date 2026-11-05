import "dart:io";

void main(){
  print('Bienvenido a CiruPet, por favor si quiere una cita a continuacion ingrese el nombre y edad de su mascota.');
  print('Nombre:');
  String? name = stdin.readLineSync();
  print('Edad:');
  String? text2 = stdin.readLineSync()!;
  int? years = int.parse(text2);
  
  Mascota mascotas = Mascota(name, years);

  print('Excelente, su mascota ${mascotas.nombre} registrada con la edad de ${mascotas.edad} se agendara para...');
}

class Mascota{
  String? nombre;
  int? edad;
  Mascota(this.nombre, this.edad);
}