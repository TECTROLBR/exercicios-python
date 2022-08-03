print('      PROGREÇÃO ARITMETICA PA')
print('*=-'*12)
termo = int(input('Primeiro termo: '))
rasao = int(input('Rasão: '))
cd = termo + 10 * rasao
for c in range(termo, cd, rasao):
    print(c, end='*')
print('FIM')
