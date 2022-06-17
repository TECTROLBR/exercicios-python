km = int(input('qual a distancia em da sua viagem? km '))
if km <= 200:
    print('sera cobrado {:.2f}R$ pelos {} km'.format(km*0.50,km))
else:
    print('sera cobrado {:.2f}R$ pelos {} km'.format(km*0.45,km))
