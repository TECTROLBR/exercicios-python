num = cont = total=  0
num=int(input('Digite um numero ou 999 para sair: '))
while num != 999:
    total += num
    cont +=1
    num = int(input('Digite um numero ou 999 para sair: '))
print('Você digitou {} e a soma dele e {}'.format(cont, total))