print('     DESAFIO DO TRIAGULO')
lado1 = float(input('Insira o primeiro lado = '))
lado2 = float(input('Insira o segundo lado = '))
lado3 = float(input('Insira o terceiro lado = '))
if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado2 + lado3 < lado1 :
    print('Nao pode forma um triagulo')
elif lado1 == lado2 and lado1 == lado3 :
    print('Forma um triagulo EQUILÁTERO!')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
    print('Forma um triangulo ISÓRCELIS!')
elif lado1 != lado2 or lado1 != lado3 or lado2 != lado3 :
    print('Forma um triangulo ESCALENO!')