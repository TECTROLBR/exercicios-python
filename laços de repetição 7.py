from datetime import date
maior = 0
menor = 0
atua = date.today().year
for dat in range(1, 8):
    ano=int(input('digite o {}°ano: '.format(dat)))
    res = atua - ano
    if res >= 21:
        maior+=1
    if res <=20:
        menor+=1
print('{} Dos informafos são menores de idade\nE {} São maiores de idade'.format(menor, maior))
