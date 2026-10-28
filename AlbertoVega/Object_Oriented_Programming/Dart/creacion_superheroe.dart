import "dart:io";

void main(){
  print("¡ALERTA DE VILLANO, INGRESE SU NOMBRE Y PODER A CONTINUACION PARA PODER DAR UNA VISO DE QUE HA LLEGADO USTED PARA SALVAR LA CIUDAD!");
  print("DIGITE SU NOMBRE:");
  String? name = stdin.readLineSync();
  print("QUERIDO SEÑOR/A ${name} RAPIDO, INGRESE SU PODER PARA QUE PUEDA SALVAR LA CIUDAD:");
  String? power = stdin.readLineSync();

  Superheroe heroe = Superheroe(name, power);

  print("¡ALERTA EL HEROE ${heroe.nombre} HA VENIDO A SALVAR LA CIUDAD CON SU PODER ${heroe.poder}");
}


class Superheroe{
  String? nombre;
  String? poder;
  Superheroe(this.nombre, this.poder);
}