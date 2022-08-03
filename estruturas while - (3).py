from time import sleep
opçao = ''
n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
while opçao != 5:
      print('O que você quer fazer?\n'
            '[1] Somar\n'
            '[2] Mutiplicar\n'
            '[3] Quer ver quem e o maior\n'
            '[4] Quer novos numeros\n'
            '[5] Sair do programa\n')
      opçao = int(input('entao o que vai ser? '))
      if opçao > 5:
            print('opção invalida tentar novamente!')
            sleep(1)
      if opçao == 1:
            print('{} +{} = {}'.format(n1,n2,n1+n2))
            sleep(2)
      if opçao ==2:
            print('{} x {} = {}'.format(n1,n2,n1*n2))
            sleep(2)
      if opçao == 3:
            if n1 > n2:
                  print('{} E maior que {}'.format(n1,n2))
            else:
                  print('{} e maior que {}'.format(n2,n1))
            sleep(2)
      if opçao == 4:
            print('insira novamente os valores!')
            n1 = int(input('1° valor: '))
            n2 = int(input('2° valor: '))
print(f'Finalizando...')
sleep(2)
print('Você encerrou o programa')
print('          THAL!!')
