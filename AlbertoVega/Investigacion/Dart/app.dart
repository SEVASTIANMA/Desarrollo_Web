import 'dart:io';

void main(){
  print('Digite las 5 notas del periodo:');
  print('[1]:');
  String? note1 = stdin.readLineSync();

  print('[2]:');
  String? note2 = stdin.readLineSync();

  print('[3];');
  String? note3 = stdin.readLineSync();

  print('[4]:');
  String? note4 = stdin.readLineSync();

  print('[5]:');
  String? note5 = stdin.readLineSync();

  int suma = int.parse(note1!) + int.parse(note2!);
  int suma2 = suma + int.parse(note3!) + int.parse(note4!);
  int sumaTotal = suma2 + int.parse(note5!);
  
  int promedioFinal = sumaTotal ~/ 5;
  print('Su total es: $promedioFinal');
}