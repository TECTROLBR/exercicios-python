from math import hypot
catop = float(input('digite o cateto oposto? = '))
catad = float(input('digite o cateto adijacente? = '))
cal = hypot(catad, catop)
print('o valor da hipotenusa {:.2f}'.format(cal))