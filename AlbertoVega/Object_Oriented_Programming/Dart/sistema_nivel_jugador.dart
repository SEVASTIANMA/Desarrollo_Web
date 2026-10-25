import "dart:io";

void main(){
  void main(){
  print("Bienvenido Guerrero, a continuacion para poder ingresar al gremio necesitamos que digite su nombre y su nivel a continuacion.");
  print("Nombre:");
  String? name = stdin.readLineSync();
  print("Señor/a ${name}, digite su nivel para poder terminar y determinar su poder.");
  String? text1 = stdin.readLineSync()!;
}

class Guerrero{
  String? nombre;
  int? nivel;
  
  Guerrero(this.nombre, this.nivel);

}