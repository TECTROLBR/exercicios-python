sal = float(input('qual o seu salario? R$ '))
if sal >= 1250.00:
    print('seu novo salario com 10% de almento fica R$ {:.2f}'.format(sal+(sal*10/100)))
else:
    print('seu novo salario com 15% de almento fica R$ {:.2f}'.format(sal+(sal*15/100)))