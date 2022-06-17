frase = str(input('digite seu nome! ')).strip()
f1 = frase.split()
print('primeiro nome e {}\nsegundo nome e {}'.format(f1[0],f1[len(f1)-1]))