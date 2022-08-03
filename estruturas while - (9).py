cont = num = total  =medi =maior =menor = 0
sair = ' '

while sair not in 'nN':

    num=int(input('digite um numero? : '))
    cont += 1
    if cont == 1:                           # vai colocar o valor como maior e menor na primeira contagem
        maior = menor = num
    else:                                          # quando altera a contagem vai conpara os valores
        if num > maior:               # se o numero for maior atualiza a variavel maior
            maior = num
        if num < menor:              # se o numero for menor atualisa a variavel menor
            menor = num
    total += num
    medi = float(total/cont)
    sair = input('deseja continuar? (S/N) : ').strip()

    while sair not in 'SsnN':
        print('escolha invalida!!')
        sair = input('deseja continuar? (S/N) : ').strip()

print("Voce digitou {} numeros e a media e {:.2f}".format(cont, medi))
print( 'o menor numero digitado foi {} e o  maior {}'.format(menor,maior))
