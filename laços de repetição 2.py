soma = 0
contado = 0
for inpa in range(1,501,2):
    if inpa % 3 == 0:
        soma = soma + inpa
        contado = contado + 1
print('todos os {} numeros devisivel por 3 soma um tota de {}'.format(contado,soma))
