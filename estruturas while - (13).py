from time import sleep

contua = 'S'
idade =desoito=masculino=mulhevinte=0
while True:
    print('**'*9)
    print('** novo  cadastro **')
    print('**'*9)
    idade = int(input('Idade : '))
    sexo = str(input('Sexo : [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo : [M/F] ')).upper().strip()[0]
    contua = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    while contua not in 'SN':
        contua = str(input('quer continuar? [S/N] ')).upper().strip()[0]
    if idade >= 18:
        desoito +=1
    if sexo == 'M':
        masculino+=1
    if sexo == 'F':
        if idade <=20:
            mulhevinte+=1
    if contua =='N':
        break

print('PROGAMA ENCERRADO')
print('carregando DADOS...')
sleep(2)
print(f'Ha {desoito} pessoas no cadastro com mas de 18 anos.\nTem {masculino} Homens cadastrado.\nTem {mulhevinte} mulheres com mesnos de 20 anos.')