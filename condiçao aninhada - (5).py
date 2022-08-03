from random import randint
from time import sleep
print('   JOKEMPO')
print('[1] = tesoura\n[2] = papel\n[3] = pedra')
iten = ('tesoura', 'papel', 'pedra')
conputado = randint(1, 3)
jogado = int(input('Qual sua escolha? '))
if jogado >= 4:
    print('\033[31m    ESCOLHA INVALIDA\nPORFAVOR ESCOLHA ENTRE 1 E 3!!\033[m')
print('JO!!')
sleep(1)
print('KEM!!')
sleep(1)
print('POOO!!')
print('VOCÊ ESCOLÇHEU >:{}\nCOMPUTADOR ESCOLHEU >:{}'.format(iten[jogado],iten[conputado]))
if conputado == 1:#tesoura
   if jogado == 1:
       print('EMPATE!!')
   if jogado == 2:
       print('VOCÊ PERDEU!!!')
   if jogado == 3:
       print('VOCÊ GANHOU!!!')
if conputado == 2:#papel
    if jogado == 1:
        print('VOCÊ GANHOU!!!')
    if jogado == 2:
        print('EMPATE!!')
    if jogado == 3:
        print('VOCÊ PERDEU!!!')
if conputado == 3:#pedra
    if jogado == 1:
        print('VOCÊ PERDEU!!!')
    if jogado == 2:
        print('VOCÊ GANHOU!!!')
    if jogado == 3:
        print('EMPATE!!')