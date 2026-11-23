void main(){
  Computador lenovo = new Computador(a: "900gb", c: "AMD Ryzen 7 7000", r: 32, g: "RTX 3060");
    lenovo.teclado = "Teclado logitech a bluethoot";
    lenovo.mouse = "Mouse logitech USB";
    lenovo.so = "Windows 11";
    lenovo.navegador = "Brave";
    print("Computador gamer ${lenovo.so}, procesador ${lenovo.cpu} con tarjeta grafica ${lenovo.gpu}, ${lenovo.ram}gb de RAM, ${lenovo.almacenamiento} de almacenamiento.");
    print("Incluye: ${lenovo.teclado}, ${lenovo.mouse} y navegador predeterminado ${lenovo.navegador}.");
}

class Computador{
  String? teclado;
  String? mouse;
  String? so;
  String? gpu;
  int? ram;
  String? navegador
  String? cpu;
  String? almacenamiento;

  Computador({required String g, required int r, required String c, required String a}){
    this.gpu = g;
    this.ram = r;
    this.cpu = c;
    this.almacenamiento = a;
  }
}