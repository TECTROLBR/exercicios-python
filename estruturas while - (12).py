from random import uniform
from time import sleep

print('-=-'*11)
print('-=-  VAMOS JOGA PAR OU IMPAR  -=-')
print('-=-'*11)
conp = player = vitoria = derrota = resu =escolha=0
P = 'PAR'
I = 'IMPAR'
while True:
    player = int(input('digite um numero: '))
    escolha = str(input('PAR OU IMPAR? [I / P]: ')).strip().upper()[0]
    if escolha not in 'PpIi':
        print('escolha errada! P para PAR ou I para IMPAR ')
        escolha = str(input('PAR OU IMPAR? [I / P]: ')).strip().upper()[0]
    conputa = int(uniform(1,10))
    resultado = (conputa+player)%2
    if resultado == 0:
        resu = P
    if resultado == 1:
        resu = I
    print('procesando...'),sleep(2)
    print(f'Voçe jogou {player} e o conputador {conputa} resultado foi {player+conputa} que deu {resu} ')
    if resultado ==0 :
        if escolha == 'P':
            print('voçe ganhou!!!')
            print('Voçe pode joga novamente')
            vitoria+=1
        else:
            break
    if resultado == 1 :
        if escolha == 'I':
            print('voçe ganhou!!!')
            print('Voçe pode joga novamente')
            vitoria+=1
        else:
            break
print(f'GAME OVER\n Voçe venceu {vitoria} vezes.')
