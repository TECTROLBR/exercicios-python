dias =int(input('quantos dias foi alugado? '))
km = float(input('quantos quilometros rodados? '))
cal = 60*dias+km*0.15
print('o valor a ser pago e de R${:.2f}'.format(cal))