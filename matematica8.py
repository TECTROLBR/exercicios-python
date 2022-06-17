salario = float(input('qual o salario do funcionario?R$ '))
aume = salario + (salario*15/100)
print('o salario de {:.2f}R$ com um novo aumento de 15%\npassa a ser de {:.2f}R$'.format(salario, aume))