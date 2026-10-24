class Estudiante {
  String persona;
  Estudiante(this.persona);
}

void main() {
  List<Estudiante> estudiantes = [];

  for (int i = 1; i <= 1500; i++) {
    estudiantes.add(Estudiante('Persona$i'));
  }

  for (var estudiante in estudiantes) {
    print(estudiante.persona);
  }
}