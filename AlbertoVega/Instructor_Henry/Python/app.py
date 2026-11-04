def main():
    print('Ingrese a continuacion las 5 notas del periodo academico:')
    nota1 = int(input('[1]: '))
    nota2 = int(input('[2]: '))
    nota3 = int(input('[3]: '))
    nota4 = int(input('[4]: '))
    nota5 = int(input('[5]: '))


    suma = nota1 + nota2 + nota3 + nota4 + nota5
    promedioFinal = suma / 5
    
    print(f'Nota final: {promedioFinal}')


if __name__ == '__main__':
    main()