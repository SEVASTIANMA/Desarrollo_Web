void main() {
  Carros carro = new Carros();
  carro.placa = 'MTR-456';
  carro.modelo = 2021;
  carro.auto = true;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto: ${carro.auto}');
}

class Carros {
  String? placa;
  int? modelo;
  bool? auto;
}
