nu = sequ = 0

while True:
    nu = int(input('qual a tabuada a ser mostrada: '))
    if nu < 0:
        break
    while sequ != 10:
        sequ += 1
        resu = nu * sequ
        print(f'{nu} X {sequ} = {resu}')
    if sequ == 10:
        sequ = sequ - 10
print('-*-'*10)
print('fim da tabuada')
