saldo = 0
print('/'*25)
print('boca do caixa'.center(22).upper())
print('/'*25)
print('seja bem vindo'.upper().center(22))
print('///'.center(29))
usuario= str(input('usuario: '.upper()))
senha= int(input('senha: '.upper()))
print(f'bem vindo {usuario.upper()}')
saldo = float(input('Quanto quer sacar: R$ '))
cedu = 50
contacedula = 0
res = ' '
while True:
    if saldo >= cedu:
        saldo-=cedu
        contacedula +=1
    else:
        if contacedula > 0:
            print(f'total de {contacedula} cedulas de {cedu}')
        if cedu == 50:
            cedu = 20
        elif cedu == 20:
            cedu = 10
        elif cedu == 10:
            cedu = 1
        contacedula = 0
        if saldo == 0:
          break

