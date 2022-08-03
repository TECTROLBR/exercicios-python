from time import sleep
bara = ''
n = total = mil=menopreço = 0
while True:
    n += 1
    print('-+'*8)
    print('-+ Novo produto. -+')
    print('-+'*8)
    nome = str(input(f'Nome do produto {n}: ')).title()
    preço = float(input('Preço: R$ '))
    total += preço

    if n == 1:
       menopreço = preço
       bara = nome
    else:
        if preço < menopreço:
            menopreço = preço
            bara = nome

    if preço >= 1000:
        mil+=1

    confirmaçao = str(input('Tem mas produtos?[S/N]: ')).upper().strip()[0]
    while confirmaçao not in 'SN':
        confirmaçao = str(input('Tem mas produtos?[S/N]: ')).upper().strip()[0]
    if confirmaçao == 'N':
        break
print('Conpra finalizada')
print('Calculando nota de compra...')
sleep(2)
print(f'Total da compra foi de R${total:.2f}')
if mil == 0:
    print('Nao ha produtos que custa mas de R$ 1000.00')
else:
    print(f'Ha {mil} Produtos que custa mais de R$1000.00')
print(f'O item mas barato e uma {bara} que custa R${menopreço:.2f} ')