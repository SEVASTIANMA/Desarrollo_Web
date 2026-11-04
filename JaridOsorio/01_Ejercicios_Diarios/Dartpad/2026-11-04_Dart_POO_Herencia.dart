// ==========================================
// Herencia y Polimorfismo en Dart
// ==========================================

void main() {
  Persona aprendiz = AprendizSENA("Jarid", 20, "ADSO");
  aprendiz.presentarse();
}

// Clase Base (Superclase)
class Persona {
  String nombre;
  int edad;

  Persona(this.nombre, this.edad);

  void presentarse() {
    print('Hola, mi nombre es $nombre y tengo $edad años.');
  }
}

// Clase Derivada (Subclase)
class AprendizSENA extends Persona {
  String programa;

  AprendizSENA(String nombre, int edad, this.programa) : super(nombre, edad);

  @override
  void presentarse() {
    super.presentarse();
    print('Me encuentro cursando el tecnólogo en $programa en el SENA 🚀.');
  }
}