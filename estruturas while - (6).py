print('=-='*6)
print('=-=  Gerador de PA  =-=')
print('=-='*6)

termo = int(input('Qual o primeiro termo: '))
razão = int(input('Qual a PA: '))
retorno = 1
pa = termo
mais = 10
conclusao = 0
while mais != 0:
    conclusao += mais
    while retorno <= conclusao:
        print('{} - '.format(pa), end='')
        pa += razão
        retorno +=1
    print('PAUSA')
    mais = int(input('Quanta PA a mas quer ver: '))
print(f'o total da PA mostrado foi {conclusao}')