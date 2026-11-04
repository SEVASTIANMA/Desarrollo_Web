import "dart:io";

void main(){
  print("Bienvenido usuario, digite su nombre completo.");
  print("Nombre:");
  String? nameleido = stdin.readLineSync();
  print("Apellido");
  String? apellidoleido = stdin.readLineSync();
  print("Excelente señor/a ${nameleido} ${apellidoleido}. Para finalizar por favor ingrese su edad a continuacion:");
  int? edadleida = int.parse(stdin.readLineSync()!);

  Usuario usuario = Usuario(nameleido, apellidoleido, edadleida);

  print("Usuario registrado y creado con exito, puede pasar señor/a ${usuario.name} ${usuario.apellido} con ${usuario.edad} años de edad");
}

class Usuario{
  Usuario(this.name, this.apellido, this.edad,);
  String? name;
  String? apellido;
  int? edad;
}