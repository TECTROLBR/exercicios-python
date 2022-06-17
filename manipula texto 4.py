frase = input('degite uma farse! ').strip().upper()
con = frase.count('A')
pro1 = frase.find('A')+1
pro2 = frase.rfind('A')+1
print('neta frase tem {} letras "A"\ne a primeira letra "A" esta na {} casa\ne a ultma letra "A"esta na {} casa!'.format(con,pro1,pro2))