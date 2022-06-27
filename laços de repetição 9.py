femin = 0
velho = 0
nomevelho = ''
novamulher = 0
media = 0
for pessoas in range(1,5):
    print('*===== {}ªPESSOA =====*'.format(pessoas))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    gener = str(input('sexo (M/F): ')).strip()
    media += idade
    if pessoas == 1 and gener in 'mM':
        velho = idade
        nomevelho = nome
    if gener in 'mM' and idade > velho:
        velho = idade
        nomevelho = nome
    if gener in 'fF' and idade <20:
        novamulher+=1
media = media / 4
print('A idade media desse grupo e de {:.2f}'.format(media))
print('O home mas velho e {} e tem {} anos'.format(nomevelho, velho))
print('E tem {} mulheres abaixo de 20 anos'.format(novamulher))