cat=float(input('quanto vc tem na carteira?R$ '))
dolar= cat/3.27 #valores mudam dia a dia ou ah qualquer hora!
euro= cat/5.25
libra= cat/6.14
print('com {} da para conpra em? \ndolar {:.2f}\neuro {:.2f}\nlibra {:.2f}'.format(cat,dolar,euro,libra))