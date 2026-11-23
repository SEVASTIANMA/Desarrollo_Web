void main(){

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

  Computador({required String g, required int r, required String c, required String a}){
    this.gpu = g;
    this.ram = r;
    this.cpu = c;
    this.almacenamiento = a;
  }
}