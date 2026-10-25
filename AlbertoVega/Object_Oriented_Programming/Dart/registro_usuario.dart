import "dart:io";

void main(){
  print("Bienvenido usuario, digite su nombre completo.");
  print("Nombre:");
  String? nameleido = stdin.readLineSync();
  print("Apellido");
  String? apellidoleido = stdin.readLineSync();
  print("Excelente señor/a ${nameleido} ${apellidoleido}. Para finalizar por favor ingrese su edad a continuacion:");
}

class Usuario{
  Usuario(this.name, this.apellido, this.edad,);
  String? name;
  String? apellido;
  int? edad;
}