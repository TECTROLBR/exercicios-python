from datetime import date
print('     Analizando da categoria de natação')
ano = int(input('Digite o ano de nacimento? '))
idade = int (date.today().year)-ano
if idade <= 9 :
    print('vecê tem {} anos e esta na categoria MIRIM!'.format(idade))
elif idade > 9 and idade < 14 :
    print('Você tem {} anos e esta na categoria INFANTIL!'.format(idade))
elif idade >= 14 and idade < 19 :
    print('Você tem {} anos e esta na categotia JUNIO!'.format(idade))
elif idade >=19 and idade < 25 :
    print('Você tem {} anos e esta na categoria SÊNIO!'.format(idade))
elif idade >= 25 :
    print('Você tem {} anos e esta na categoria MASTER!'.format(idade))
