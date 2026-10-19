void main() {
  Car car = new Car();
  car.placa = "ABC-01";
  car.modelo = 1990;
  car.auto = false;
  print("La descripcion del primer vehiculo es: ${car.placa} , ${car.modelo} , ${car.auto}");

  Car car2 = new Car();
  car2.placa = "DEF-02"; 
  car2.modelo = 1995; 
  car2.auto = true; 
  print("La descripcion del segundo vehiculo es: ${car2.placa} , ${car2.modelo} , ${car2.auto}");

  Car car3 = new Car();
  car3.placa = "GHI-03"; 
  car3.modelo = 2000;  
  car3.auto = false;    
  print("La descripcion del tercer vehiculo es: ${car3.placa} , ${car3.modelo} , ${car3.auto}");

  Car car4 = new Car();
  car4.placa = "JKL-04"; 
  car4.modelo = 2005;   
  car4.auto = true;     
  print("La descripcion del cuarto vehiculo es: ${car4.placa} , ${car4.modelo} , ${car4.auto}");

  Car car5 = new Car();
  car5.placa = "MNO-05"; 
  car5.modelo = 2010;   
  car5.auto = false;   
  print("La descripcion del quinto vehiculo es: ${car5.placa} , ${car5.modelo} , ${car5.auto}");
}

class Car {
  String? placa;
  int? modelo;
  bool? auto;
}