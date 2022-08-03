import time

n = int(input('degite um numero: '))
r = n
f = 1
print('o fatorial de {}!'.format(n))
while r > 0:
    print('{} '.format(r), end='')
    print(' x 'if r > 1 else ' = ', end='')
    f *= r
    r = (r-1)
    time.sleep(0.1)
print(f)