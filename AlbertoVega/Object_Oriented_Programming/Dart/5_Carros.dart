void main() {
  Carros carro = new Carros();
  carro.placa = 'MTR-456';
  carro.modelo = 2021;
  carro.auto = true;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto: ${carro.auto}');

  Carros carro = new Carros();
  carro.placa = 'BQA-789';
  carro.modelo = 2021;
  carro.auto = false;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto: ${carro.auto}');

  Carros carro = new Carros();
  carro.placa = "KLO-234";
  carro.modelo = 2021;
  carro.auto = true;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto ${carro.auto}');

  
}

class Carros {
  String? placa;
  int? modelo;
  bool? auto;
}
