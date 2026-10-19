void main() {
  Nombres nombres = new Nombres(); 
  
  for (int i = 1; i <= 1500; i++) {
    nombres.imprimir(i); 
  }
}
class Nombres {
  void imprimir(int numero) {
    print('Nombre $numero');
  }
}