import random
import time
print('-'*45)
pen = int(input('de 0 a 5 qual o conputador esta pençando? = '))
print('-'*15)
n = [0,1,2,3,4,5]
ale  =int(random.choice(n))
print('PROSESANDO...')
time.sleep(1.5)
if pen >= int('6'):
    print('numero ivalido')
else:
    print('o resultado foi {}'.format(ale))
if pen == ale :
    print('voçê acertou')
else:
    print('voçê errou')