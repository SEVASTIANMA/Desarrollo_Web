class Person {}
void main() {
  final Person = List.generate(1500, (_) => Person());

  for (int i = 1; i <= 1500; i++) {
    print('Objeto $i');
  }
}