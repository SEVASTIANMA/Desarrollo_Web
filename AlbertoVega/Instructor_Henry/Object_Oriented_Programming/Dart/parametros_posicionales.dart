void main(){
  Computador lenovo = new Computador("RTX 3060", 16, "AMD Ryzen 7 7000", "900gb");
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
  String? navegador;
  String? cpu;
  String? almacenamiento;

  Computador(String g, int r, String c, String a){
    this.gpu = g;
    this.ram = r;
    this.cpu = c;
    this.almacenamiento = a;
  }
}