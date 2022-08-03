nume = cont = total =0
while True:
    print('para sair digite 999!!')
    nume = int(input('digite um numero: '))
    if nume == 999:
        break
    total += nume
    cont +=1

print(f'foi digitado {cont} numeros e o valor total e {total}')
