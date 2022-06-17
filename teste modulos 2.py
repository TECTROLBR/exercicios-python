from math import cos, sin, tan, acos, asin, atan, radians
graus = int(input('digite um valor para medir sua trigometria ='))
rad = radians(graus)
print('o seu valor em cosseno {:.2f}'.format(cos(rad)))
print('o seu valor em seno {:.2f}'.format(sin(rad)))
print('o seu valor em tangente {:.2f}'.format(tan(rad)))
print('o seu valor em arco coseno {:.2f}'.format(acos(rad)))
print('o seu valor em arco seno {:.2f}'.format(asin(rad)))
print('o seu valor em arco tangete {:.2f}'.format(atan(rad)))