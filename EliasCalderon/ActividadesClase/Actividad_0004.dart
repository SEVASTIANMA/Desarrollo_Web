 void main() {
  Car car1 = new Car();
  car1.Placa = 'AHJ-897';
  car1.Modelo = 2024;
  car1.Automatico = false;
  print('Carro 1 - placa: ${car1.Placa} Modelo: ${car1.Modelo} Automtico: ${car1.Automatico}');

   Car car2 = new Car();
  car2.Placa = 'KLQ-765';
  car2.Modelo = 2026;
  car2.Automatico = false;
  print('Carro 2 - placa: ${car2.Placa} Modelo: ${car2.Modelo} Automtico: ${car2.Automatico}');


 Car car3 = new Car();
  car3.Placa = 'VBN-555';
  car3.Modelo = 2018;
  car3.Automatico = true;
  print('Carro 3 - placa: ${car3.Placa} Modelo: ${car3.Modelo} Automtico: ${car3.Automatico}');


 Car car4 = new Car();
  car4.Placa = 'MKL-833';
  car4.Modelo = 2012;
  car4.Automatico = false;
  print('Carro 4 - placa: ${car4.Placa} Modelo: ${car4.Modelo} Automtico: ${car4.Automatico}');

 Car car5 = new Car();
  car5.Placa = 'LPO-456';
  car5.Modelo = 2024;
  car5.Automatico = true;
  print('Carro 5 - placa: ${car5.Placa} Modelo: ${car5.Modelo} Automtico: ${car5.Automatico}');

}
class Car{
  String? Placa;
  int? Modelo;
  bool? Automatico;
}