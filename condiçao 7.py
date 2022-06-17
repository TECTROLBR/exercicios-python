r1 = float(input('primeira reta? = '))
r2 = float(input('segunda reta? = '))
r3 = float(input('terceira reta? = '))
if r1 + r2 < r3 and r1 + r3 < r2 and r2 + r3 < r1:
    print('não e um triangulo')
else:
    print('e um triangulo')
