class Carro {
  String placa;
  String marca;
  bool automatico;

  Carro(this.placa, this.marca, this.automatico);

  void mostrarInformacion() {
    print("Placa: $placa");
    print("Marca: $marca");
    print("¿Es automático?: ${automatico ? "Sí" : "No"}");
    print("-------------------------");
  }
}

void main() {
  List<Carro> carros = [
    Carro("ABC123", "Toyota", true),
    Carro("DEF456", "Chevrolet", false),
    Carro("GHI789", "Mazda", true),
    Carro("JKL012", "Renault", false),
    Carro("MNO345", "Kia", true),
  ];

  print("=== LISTA DE 5 CARROS ===");
  print("");

  for (var carro in carros) {
    carro.mostrarInformacion();
  }
}