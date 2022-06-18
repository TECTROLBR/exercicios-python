print('\033[31m     CALCULO DE CONVERÇÃO BINÁRIA/OCTAL/HEXADECIMAL\033[m')
numero = int(input('Porfavo digite o numero para converção? = '))
escolha = int(input('1-Para binário\n2-Para octal\n3-Para hexadecimal\nSua escolha e = '))
binário = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
if escolha == 1 :
    print('Sua escolha foi binário')
    print('O valor para binário e = {}'.format(binário))
elif escolha == 2 :
    print('Sua escolha foi octal')
    print('O valor para octal e = {}'.format(octal))
elif escolha == 3 :
    print('Sua escolha foi hexadecimal')
    print('O valor para hexadecimal e = {}'.format(hexadecimal))