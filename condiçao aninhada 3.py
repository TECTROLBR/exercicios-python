from  datetime import date
print('        TENPO DE ALISTAMENTO')
idade = int(input('Em que anos você naceu? '))
anoatual=int (date.today().year)
calculodata = anoatual-idade
if calculodata == 18 :
    print('Você ja tem idade para se alistar')
elif calculodata < 18 :
    print('Você vai se  alistamente em {}'.format(idade+18))
    print('Ainda falta {} anos para você se alistar'.format(calculodata))
elif calculodata > 18 :
    print('Você nao pode mas se alistar\nDeveria ter se alistado {}'.format(idade+18))
