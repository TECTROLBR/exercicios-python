escolha = str(input('Escolha seu sexo?[M/F]: ')).strip().upper()[0]
while escolha not in 'FfMm':
    escolha = str(input('informação errada! escolha  sexo?[M/F]: ')).strip().upper()[0]
if escolha == 'F':
    print('Você e mulher')
if escolha == 'M':
    print('Você e homem')
