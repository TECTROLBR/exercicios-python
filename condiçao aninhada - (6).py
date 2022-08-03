from time import sleep
print('+=-'*10)
print('+=-\033[4:33:40m SIMULADO DE EMPRESTIMO\033[m +=-')
print('+=-'*10)
valorcasa = float(input(' Qual o valor da casa? R$\033[1:32m''\033[m'))
salario = float(input('qual o valor do seu salario?\033[1:32m''\033[m'))
tempopaga = int(input('em quantos anos quer paga o enprestimo?\033[1:32m''\033[m'))
presta = tempopaga*12

valmesa = valorcasa / presta

neg30 = float(salario-(salario-(salario*30/100)))
print(' '*5,'+=-'*7)
print(' '*5,'+=-\033[4:33:40mPROCESANDO....\033[m +=-')
print(' '*5,'+=-'*7)
sleep(3.5)
if neg30 < valmesa:
    print('+=-'*11)
    print('+=- \033[7:41m SEU ENPRETIMO FOI NEGADO\033[m +=-')
    print('+=-'*11)
    print('\033[34mMude a quantidade de tenpo a pagar!\033[m')
else:
    print('+=-'*12)
    print('+=- \033[34mSEU ENPRESTIMO FOI APROVADO\033[m  +=-')
    print('+=-'*12)
    print('Uma casa num valor de {:.2f}R$'.format(valorcasa))
    print('Voçê pagara \033[31m{}\033[m vezer de \033[31m{:.2f}R$\033[m'.format(presta,valmesa))