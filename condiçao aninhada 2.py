print('ANALIZADOR DE NÚMEROS')
n1 = int(input('Digite o primeiro número? '))
n2 = int(input('Digite o segundo número? '))
if n1 > n2:
    print('O primeiro NÚMERO e maior')
elif n2 > n1:
    print('O segundo NÚMERO e maior')
elif n1 == n2:
    print('Os NÚMEROS são iguais')
