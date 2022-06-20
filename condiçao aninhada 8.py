print('   FORMAS DE PAGAMENTO')
valor = float(input('Digite o valor do produto R$ '))
print('   Escolha a forma de pagamento?')
print('Digite \033[31m1\033[m-Avista dinheiro ou cheque. Tem 10% de desconto\nDigite \033[31m2\033[m-Avista cartão. '
      'Tem 5% de desconto\ndigite \033[31m3\033[m-2X no cartão. Sem juros\nDigite \033[31m4\033[m-3X ou mais no cartão. '
      'Tem 20% de juros')
escolha = int(input('Sua escolha foi = '))
if escolha == 1 :
    print('Você escolheu avista com 10% desconto o valor a ser pago \033[031m{:.2f}\033[mR$'.format(valor-(valor*10/100)))
elif escolha == 2 :
    print('Você escolheu avista no cartão com 5% de desconto o valor a ser pago e \033[31m{:.2f}\033[mR$'.format(valor-(valor*5/100)))
elif escolha == 3 :
    print('Será dividido {}R$ Sem juros em 2X de {:.2f}R$ no cartão'.format(valor,valor/2))
elif escolha == 4:
    print('Digite em quantas veses quer parcelar?')
    parcela = int(input(' > '))
    print('Será dividido {:.2f}R$ com 20% de juros em {}X de {:.2f}R$'.format(valor+(valor*20/100),parcela,(valor+(valor*20/100))/parcela))
