void main(){
  print('----------------CARROS----------------');
  Carros carro = new Carros();
  carro.placa = 'MTR-456';
  carro.modelo = 2021;
  carro.auto = true;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto: ${carro.auto}');
  print('---------------------------------------');
  carro.placa = 'BQA-789';
  carro.modelo = 2021;
  carro.auto = false;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto: ${carro.auto}');
  print('---------------------------------------');
  carro.placa = "KLO-234";
  carro.modelo = 2021;
  carro.auto = true;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto ${carro.auto}');
  print('---------------------------------------');
  carro.placa = 'JXZ-901';
  carro.modelo = 2018;
  carro.auto = false;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto: ${carro.auto}');
  print('---------------------------------------');
  carro.placa = "GHL-567";
  carro.modelo = 2026;
  carro.auto = true;
  print('Placa: ${carro.placa} Modelo: ${carro.modelo} Auto ${carro.auto}');
  print('---------------------------------------');
}

class Carros {
  String? placa;
  int? modelo;
  bool? auto;
}
