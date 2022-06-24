numero = int(input('digite um numero: '))
divi = 0
for c in range(1, numero+1):
      if numero % c == 0:
          print('\033[31m',end=' ')
          divi += 1
      else:
          print('\033[m',end=' ')
      print(c, end=' ')
print('\n\033[m')
if divi == 2:
    print('O numero {} e primo'.format(numero))
else:
    print('este numero {} nao e primo por ser divisivel por {}X'.format(numero,divi))