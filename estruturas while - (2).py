import random
tentativa = 1
aleatorio = random.randint(1,10)
print('ESCOLHENDO NUMERO.....')
print('Seu conputador acabou de pensar em um numero!')
print('Você pode adivinhar em qual numero de 1 a 10 que ele escolheu?')
player = int(input('qual você escolhe: '))
while player != aleatorio:
    if player > aleatorio:
        print('{} E maior'.format(player))
    if player < aleatorio:
        print('{} E menor'.format(player))
    print('Escolha errada!')
    player=int(input('Escolha novamente: '))
    tentativa+=1
if tentativa > 1:
    print('Parabens você acertou\nVocê tentou {} vezes\nTente fazer em menos tentativas kkk!!!'.format(tentativa))
else:
    print('Parabens você acertou de primeira!!!'.format(tentativa))